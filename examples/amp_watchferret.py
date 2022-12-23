from datetime import datetime
from time import sleep
from dotenv import load_dotenv
import os

from ampapi_handler import AMPAPIHandler

# Name of program is now "watchferret", credit to sneakysnek#8707

# Path to logs
LOGGING_PATH = "./"

# Time in seconds for how often you want to ping the server
SAMPLE_INTERVAL = 300

# Average rescue threshold in minutes: INTERVAL*THRESHOLD/60 (plus or minus ~0.95*INTERVAL/60)

# How many pings during a server restart before rescuing the server.
RESTART_THRESHOLD = 2
# How many pings during a server start before rescuing the server.
START_THRESHOLD = 10


def logger(instance_name: str, string: str) -> None:
    today = str(datetime.now().strftime("%Y-%m-%d"))
    now = str(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

    if LOGGING_PATH[-1] == "/":
        folder = LOGGING_PATH
    else:
        folder = LOGGING_PATH + "/"

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


def watchferret(instance_name):
    load_dotenv()
    username = os.getenv("AMP_API_USER")
    password = os.getenv("AMP_API_PASSWORD")

    ADS = AMPAPIHandler(
        baseUri="http://localhost:8080", # The address of your main controller/ADS
        username=username,
        password=password
    )
    ADS.initHandler()
    logger(instance_name, "Authenticating with AMP")

    for target in (ADS.ADSModule.GetInstances())["result"]:
        for instance in target["AvailableInstances"]:
            if instance["InstanceName"] == instance_name:
                instance_id = instance["InstanceID"]

                InstanceAPI = ADS.InstanceLogin(instance_id=instance_id)

                if InstanceAPI != None:
                    InstanceAPI.init()

                    logger(instance_name, "Initializing Instance connection")

                    restart_tracker = 0
                    while True:
                        try:
                            status = InstanceAPI.Core.GetStatus()["State"]

                            if status == 30:
                                restart_tracker += 1
                                start_tracker = 0
                            elif status == 10:
                                start_tracker += 1
                                restart_tracker = 0
                            else:
                                restart_tracker = 0
                                start_tracker = 0

                            logger(instance_name, f"Server Status: {status}, Restart Pings: {restart_tracker}, Start Pings: {start_tracker}")

                            if restart_tracker >= RESTART_THRESHOLD or start_tracker >= START_THRESHOLD:
                                logger(instance_name, f"Watchdog Event Detected")
                                InstanceAPI.Core.Kill()
                                sleep(10)
                                InstanceAPI.Core.Start()
                                logger(instance_name, f"Attempting to rescue: {instance_name}")

                            sleep(SAMPLE_INTERVAL)
                        except:
                            InstanceAPI.Login()

                else:
                    logger(instance_name, f"Instance Offline: {instance_name}")

if __name__ == "__main__":
    watchferret("the non-friendly instance name")
