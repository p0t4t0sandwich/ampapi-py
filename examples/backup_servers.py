#!/bin/python3

from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Process, cpu_count
import os
import random
from dotenv import load_dotenv

from datetime import datetime,timezone
import gzip

from b2sdk.v2 import B2Api, InMemoryAccountInfo

from ampapi_handler import AMPAPIHandler





class Backup(AMPAPIHandler):
    def __init__(self, baseUri: str, username: str, backup_path: str, password: str = "", rememberMeToken: str = "", sessionId: str = "") -> None:
        super().__init__(baseUri=baseUri, username=username, password=password, rememberMeToken=rememberMeToken, sessionId=sessionId)
        self.backup_path = backup_path

    def InstanceLogin(self, instance_id: str):
        loginResult = self.InstanceAPICall(
            instance_id=instance_id,
            endpoint="/API/Core/Login",
            data={
                "username": self.username,
                "password": self.password,
                "token": "",
                "rememberMe": True
            }
        )

        if "success" in loginResult.keys() and loginResult["success"]:
            return Backup(
                baseUri=self.baseUri + f"API/ADSModule/Servers/{instance_id}",
                username=self.username,
                password=self.password,
                rememberMeToken=loginResult["rememberMeToken"],
                sessionId=loginResult["sessionID"],
                backup_path=self.backup_path
            )

    # Tar and Gzip are split into separate actions because the NAS has built-in compression while B2 does not.
    def tar_to_ball(self, output_filename: str, source_dir: str) -> None:
        with open(source_dir, 'rb') as f_in, gzip.open(output_filename, 'wb') as f_out:
            f_out.writelines(f_in)
            f_out.close()

    def b2_upload(self, keyID: str, applicationKey: str, bucket_name: str, local_file: str, file_name: str) -> None:
        """Function to simplify uploading files to Backblaze B2."""
        info = InMemoryAccountInfo()
        b2_api = B2Api(info)

        b2_api.authorize_account("production", keyID, applicationKey)

        bucket = b2_api.get_bucket_by_name(bucket_name)
        bucket.upload_local_file(local_file=local_file, file_name=file_name)

    def backup_minecraft_instance(self, host: str, datastore: str, name: str, keyID: str, applicationKey: str):
        try:
            """Function designed to back up a Minecraft instance and upload it to the NAS and to B2."""
            # Server input to send an alert and to safely start the backup process.
            self.Core.SendConsoleMessage("say BACKING UP SERVER")
            self.Core.SendConsoleMessage("save-off")
            self.Core.SendConsoleMessage("save-all")

            print(f"Starting: {name}")

            # Get rid of garbo files.
            os.system(f'ssh amp@{host} "rm {datastore}/{name}/Minecraft/plugins/Skript/backups/*"')
            os.system(f'ssh amp@{host} "rm -r {datastore}/{name}/Minecraft/backups/"')

            # Datetime formatting for the Tar file.
            now = datetime.now(timezone.utc).strftime("%F-%H-%M-%S")
            tar_name = f"{name}_{now}.tar"
            os.system(f'ssh amp@{host} "tar -cf /home/amp/backup_buffer/{tar_name} {datastore}/{name}/Minecraft/"')

            # Server input to send an alert and to safely end the backup process.
            self.Core.SendConsoleMessage("say BACKUP COMPLETE")
            self.Core.SendConsoleMessage("save-on")

            # Move file to NAS buffer and delete from origin.
            os.system(f"scp amp@{host}:/home/amp/backup_buffer/{tar_name} {self.backup_path}")
            os.system(f'ssh amp@{host} "rm /home/amp/backup_buffer/{tar_name}"')

            # Gzipping the Tar file and uploading it to Backblaze B2.
            self.tar_to_ball(f"{self.backup_path}{name}.tgz", f"{self.backup_path}{tar_name}")

            self.b2_upload(
                keyID=keyID,
                applicationKey=applicationKey,
                bucket_name="mcback",
                local_file=f"{self.backup_path}{name}.tgz",
                file_name=f"{name}.tgz"
            )

            # Move Tar to NAS and remove Gzip from buffer.
            os.system(f"mv {self.backup_path}{tar_name} /mnt/nas01-1/backups/{name}")
            os.system(f"rm {self.backup_path}{name}.tgz")

            print(f"Finished: {name}")

        except Exception as e:
            print(f"Error while processing: {name}:\n{e}")

if __name__ == "__main__":
    load_dotenv()
    username = os.getenv("AMP_API_USER")
    password = os.getenv("AMP_API_PASSWORD")
    endpoint = os.getenv("B2_ENDPOINT")
    keyID = os.getenv("B2_KEY_ID")
    applicationKey = os.getenv("B2_APPLICATION_KEY")

    def handler():
        ADS = Backup(
            baseUri="http://172.16.1.172:8080/",
            username=username,
            password=password,
            backup_path="/mnt/nas01-1/backups/backup_buffer/"
        )

        executor = ThreadPoolExecutor(cpu_count() - 1)

        futures = []

        ADS.initHandler()

        # target = (ADS.ADSModule.GetInstances())["result"][0]
        for target in (ADS.ADSModule.GetInstances())["result"]:
            target_url = target["URL"]
            target_instance_id = target["InstanceId"]
            TGT = ADS.InstanceLogin(instance_id=target_instance_id)
            TGT.init()

            # Saving target datastore paths.
            tgt_ds_id_lookup = {i["Id"]:i["Directory"] for i in TGT.ADSModule.GetDatastores()["result"]}

            # Saving datastore instance sets.
            tgt_ds_inst_lookup = {i:[j["InstanceName"] for j in TGT.ADSModule.GetDatastoreInstances(i)["result"]] for i in tgt_ds_id_lookup.keys()}

                # instance = target["AvailableInstances"][2]
            for instance in target["AvailableInstances"]:
                instance_module = instance["Module"]
                instance_id = instance["InstanceID"]

                if instance_module == "Minecraft":
                    instance_name = instance["InstanceName"]
                    for i in tgt_ds_inst_lookup.keys():
                        if instance_name in tgt_ds_inst_lookup[i]:
                            instance_datastore_path = tgt_ds_id_lookup[i]
                            break

                    InstanceAPI = ADS.InstanceLogin(instance_id=instance_id)

                    if InstanceAPI != None:
                        InstanceAPI.init()

                        future = executor.submit(
                            InstanceAPI.backup_minecraft_instance,
                            target_url[7:].split(":")[0],
                            instance_datastore_path,
                            instance_name,
                            keyID,
                            applicationKey
                        )

                        futures.append(future)
                    else:
                        print(f"Instance Offline: {instance_name}")

        for future in futures:
            future.result()

    handler()