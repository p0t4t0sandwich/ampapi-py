from datetime import datetime
from multiprocessing import Process
from time import sleep
import yaml
import os

from ampapi.ampapi import AMPAPIHandler

class WatchFerret():
    def __init__(self, config_path: str):
        self.config_path = config_path
        self.instance_dict: dict = {}

        self.restart_tracker: dict = {}
        self.start_tracker: dict = {}
        self.stop_tracker: dict = {}

    def logger(self, logging_path: str, instance_name: str, string: str) -> None:
        time = datetime.now()
        today = str(time.strftime("%Y-%m-%d"))
        now = str(time.strftime("%d/%m/%Y %H:%M:%S"))

        if logging_path[-1] == "/":
            folder = logging_path
        else:
            folder = logging_path + "/"

        if not os.path.exists(folder):
            os.makedirs(folder)

        log_name = f"{folder}{instance_name}-{today}.log"

        try:
            file = open(log_name, "a")
        except:
            file = open(log_name, "w")
            file.close()
            file = open(log_name, "a")
        file.write("[" + now + "]: [" + instance_name + " Log] " + string + "\n")
        print("[" + now + "]: [" + instance_name + " Log] " + string)
        file.close()

    def get_config(self, instance_name: str) -> dict:
        with open(self.config_path, 'r') as f:
            config = yaml.safe_load(f)
            f.close()
        if instance_name in config["instances"]:
            return dict(config["global"], **config["instances"][instance_name])
        else:
            raise Exception("Config Error, instance not found in config")

    def refresh_auth(self, instance_name: str) -> None:
        instance_conf = self.get_config(instance_name)
        if instance_conf["is_ads"]:
            ADS = AMPAPIHandler(
                baseUri=instance_conf["amp_url"],
                username=instance_conf["amp_username"],
                password=instance_conf["amp_password"]
            )
            ADS.initHandler()
            self.logger(instance_conf["logging_path"], instance_name, "Authenticating with AMP")

            for target in (ADS.ADSModule.GetInstances())["result"]:
                for instance in target["AvailableInstances"]:
                    if instance["InstanceName"] == instance_name:
                        self.instance_dict[instance_name] = ADS.InstanceLogin(instance_id=instance["InstanceID"])

                        if self.instance_dict[instance_name] != None:
                            self.instance_dict[instance_name].init()
                            self.logger(instance_conf["logging_path"], instance_name, "Initializing Instance connection")
                        else:
                            self.logger(instance_conf["logging_path"], instance_name, f"Instance Offline: {instance_name}")
        else:
            self.instance_dict[instance_name] = AMPAPIHandler(
                baseUri=instance_conf["amp_url"],
                username=instance_conf["amp_username"],
                password=instance_conf["amp_password"]
            )
            self.instance_dict[instance_name].initHandler()
            self.instance_dict[instance_name].Login()
            self.logger(instance_conf["logging_path"], instance_name, "Authenticating with AMP")

    def monitor(self, instance_name: str) -> None:
        self.restart_tracker[instance_name] = 0
        self.start_tracker[instance_name] = 0
        self.stop_tracker[instance_name] = 0

        while True:
            try:
                status = self.instance_dict[instance_name].Core.GetStatus()["State"]
                instance_conf = self.get_config(instance_name)
                restart_threshold = instance_conf["restart_threshold"]
                start_threshold = instance_conf["start_threshold"]
                stop_threshold = instance_conf["stop_threshold"]

                message = f"Server Status: {status}"

                if restart_threshold != -1 and status == 30:
                    self.restart_tracker[instance_name] += 1
                    self.start_tracker[instance_name] = 0
                    self.stop_tracker[instance_name] = 0
                    message += f", Restart Pings: {self.restart_tracker[instance_name]}"
                elif start_threshold != -1 and status == 10:
                    self.start_tracker[instance_name] += 1
                    self.restart_tracker[instance_name] = 0
                    self.stop_tracker[instance_name] = 0
                    message += f", Start Pings: {self.start_tracker[instance_name]}"
                elif stop_threshold != -1 and status == 40:
                    self.stop_tracker[instance_name] += 1
                    self.restart_tracker[instance_name] = 0
                    self.start_tracker[instance_name] = 0
                    message += f", Stop Pings: {self.stop_tracker[instance_name]}"
                else:
                    self.restart_tracker[instance_name] = 0
                    self.start_tracker[instance_name] = 0
                    self.stop_tracker[instance_name] = 0

                self.logger(instance_conf["logging_path"], instance_name, message)

                if restart_threshold != -1 and self.restart_tracker[instance_name] >= restart_threshold:
                    self.logger(instance_conf["logging_path"], instance_name, f"Watchdog Event Detected On Server Restart")
                    self.restart_tracker[instance_name] = 0
                    self.instance_dict[instance_name].Core.Kill()
                    sleep(10)
                    self.instance_dict[instance_name].Core.Start()
                    self.logger(instance_conf["logging_path"], instance_name, f"Attempting to rescue: {instance_name}")
                elif start_threshold != -1 and self.start_tracker[instance_name] >= start_threshold:
                    self.logger(instance_conf["logging_path"], instance_name, f"Watchdog Event Detected On Server Start")
                    self.start_tracker[instance_name] = 0
                    self.instance_dict[instance_name].Core.Kill()
                    sleep(10)
                    self.instance_dict[instance_name].Core.Start()
                    self.logger(instance_conf["logging_path"], instance_name, f"Attempting to rescue: {instance_name}")
                elif stop_threshold != -1 and self.stop_tracker[instance_name] >= stop_threshold:
                    self.logger(instance_conf["logging_path"], instance_name, f"Watchdog Event Detected On Server Stop")
                    self.stop_tracker[instance_name] = 0
                    self.instance_dict[instance_name].Core.Kill()
                    sleep(10)
                    self.instance_dict[instance_name].Core.Start()
                    self.logger(instance_conf["logging_path"], instance_name, f"Attempting to rescue: {instance_name}")

            except:
                self.refresh_auth(instance_name)
                self.logger(instance_conf["logging_path"], instance_name, "Authenticating with AMP")

            sleep(instance_conf["sample_interval"])

    def start(self):
        with open(self.config_path, 'r') as f:
            config = yaml.safe_load(f)
            f.close()

        for instance_name in config["instances"].keys():
            self.refresh_auth(instance_name)
            Process(target=self.monitor, args=(instance_name,)).start()

if __name__ == "__main__":
    wf = WatchFerret("./config.yml")
    wf.start()
