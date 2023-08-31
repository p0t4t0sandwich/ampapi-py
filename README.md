# ampapi-python

This API allows you to communicate with AMP installations from within Python.

Documentation for available API calls can be found by appending /API to the URL of any existing AMP installation.

Support:

- Ping `@thepotatoking3452` in the `#development` channel of the [AMP Discord](https://discord.gg/cubecoders)
- My own [development Discord](https://discord.neuralnexus.dev/)

## Installation

```bash
pip install ampapi
```

or

```bash
pip install 'ampapi @ git+https://github.com/p0t4t0sandwich/ampapi-python.git'
```

You also need the following packages installed:

```bash
pip install requests aiohttp json
```

## Notes

Currently, you can only access API responses as `dict` or `list`, still trying to figure out a good way to generalize turning the JSON responses into objects (might just use class constructors as a cheap workaround).

## Examples

### CommonAPI Example

```python
from ampapi.modules.CommonAPI import CommonAPI

def main():
    # If you know the module that the instance is using, specify it instead of CommonAPI
    API = CommonAPI("http://localhost:8080/", "admin", "myfancypassword123", "")
    API.Login()

    # API call parameters are simply in the same order as shown in the documentation.
    API.Core.SendConsoleMessage("say Hello Everyone, this message was sent from the Python API!")

    currentStatus = API.Core.GetStatus()
    CPUUsagePercent = currentStatus["Metrics"]["CPU Usage"]["Percent"]

    print("Current CPU usage is: " + str(CPUUsagePercent) + "%")

main()
```

### Async CommonAPI Example

```python
import asyncio
from ampapi.modules.CommonAPI import CommonAPI

async def main():
    # If you know the module that the instance is using, specify it instead of CommonAPI
    API = CommonAPI("http://localhost:8080/", "admin", "myfancypassword123", "")
    await API.LoginAsync()

    # API call parameters are simply in the same order as shown in the documentation.
    await API.Core.SendConsoleMessageAsync("say Hello Everyone, this message was sent from the Python API!")

    currentStatus = await API.Core.GetStatusAsync()
    CPUUsagePercent = currentStatus["Metrics"]["CPU Usage"]["Percent"]

    print("Current CPU usage is: " + str(CPUUsagePercent) + "%")

asyncio.run(main())
```

### Example using the ADS to manage an instance

```python
from ampapi.modules.ADS import ADS
from ampapi.modules.Minecraft import Minecraft

API = ADS("http://localhost:8080/", "admin", "myfancypassword123")

# Get the available instances
instancesResult = API.ADSModule.GetInstances()

targets = instancesResult["result"]

# In this example, my Hub server is on the second target
# If you're running a standalone setup, you can just use targets[1]
target = targets[1]

hub_instance_id = ""

# Get the available instances
instances = target["AvailableInstances"]
for instance in instances:
    # Find the instance named "Hub"
    if instance["InstanceName"] == "Hub":
        hub_instance_id = instance["InstanceID"]
        break

# Use the instance ID to get the API for the instance
Hub = API.InstanceLogin(hub_instance_id, Minecraft)

# Get the current CPU usage
currentStatus = Hub.Core.GetStatus()
CPUUsagePercent = currentStatus["Metrics"]["CPU Usage"]["Percent"]

# Send a message to the console
Hub.Core.SendConsoleMessage("say Current CPU usage is: " + CPUUsagePercent + "%")
```

### CommonAPI Example, handling the sessionId and rememberMeToken manually (not recommended)

```python
from ampapi.ampapi import AMPAPI

try:
    API = AMPAPI("http://localhost:8080/")

    # The third parameter is either used for 2FA logins, or if no password is specified to use a remembered token from a previous login, or a service login token.
    loginResult = API.Core.Login("admin", "myfancypassword123", "", False)

    if "success" in loginResult.keys() and loginResult["success"]:
        print("Login successful")
        API.sessionId = loginResult["sessionID"]

        # API call parameters are simply in the same order as shown in the documentation.
        API.Core.SendConsoleMessage("say Hello Everyone, this message was sent from the Python API!")
        currentStatus = API.Core.GetStatus()
        CPUUsagePercent = currentStatus["Metrics"]["CPU Usage"]["Percent"]
        print(f"Current CPU usage is: {CPUUsagePercent}%")

    else:
        print("Login failed")
        print(loginResult)

except Exception as err:
    # In reality, you'd handle this exception better
    raise Exception(err)
```

## TODO

- Add a check to see if it's been 5min since the last API call, and if so, attempt to re-log
- Figure a good mehtod to turn the JSON responses into objects
