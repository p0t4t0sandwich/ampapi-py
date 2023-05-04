# ampapi-python

This API allows you to communicate with AMP installations from within Python.

Documentation for available API calls can be found by appending /API to the URL of any existing AMP installation.

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

## Async Example

```python
import asyncio
from ampapi.ampapi import AMPAPI

async def start() -> None:
    API = AMPAPI("http://localhost:8080/")

    try:
        # The third parameter is either used for 2FA logins, or if no password is specified to use a remembered token from a previous login, or a service login token.
        loginResult = await API.Core_LoginAsync("admin", "myfancypassword123", "", False)

        if "success" in loginResult.keys() and loginResult["success"]:
            print("Login successful")
            API.sessionId = loginResult["sessionID"]

            # API call parameters are simply in the same order as shown in the documentation.
            await API.Core_SendConsoleMessageAsync("say Hello Everyone, this message was sent from the Python API!")
            currentStatus = await API.Core_GetStatusAsync()
            CPUUsagePercent = currentStatus["Metrics"]["CPU Usage"]["Percent"]
            print(f"Current CPU usage is: {CPUUsagePercent}%")

        else:
            print("Login failed")
            print(loginResult)

    except Exception as err:
        print(err)

asyncio.run(start())
```

## Non-Async Example

```python
from ampapi.ampapi import AMPAPI

def start() -> None:
    API = AMPAPI("http://localhost:8080/")

    try:
        # The third parameter is either used for 2FA logins, or if no password is specified to use a remembered token from a previous login, or a service login token.
        loginResult = API.Core_Login("admin", "myfancypassword123", "", False)

        if "success" in loginResult.keys() and loginResult["success"]:
            print("Login successful")
            API.sessionId = loginResult["sessionID"]

            # API call parameters are simply in the same order as shown in the documentation.
            API.Core_SendConsoleMessage("say Hello Everyone, this message was sent from the Python API!")
            currentStatus = API.Core_GetStatus()
            CPUUsagePercent = currentStatus["Metrics"]["CPU Usage"]["Percent"]
            print(f"Current CPU usage is: {CPUUsagePercent}%")

        else:
            print("Login failed")
            print(loginResult)

    except Exception as err:
        print(err)

start()
```

## Notes on generating implementations

ampapi-python is generated using a script that parses the API spec. The `ampapai_gen.py` script under `/utils` can be used to generate future versions of the API. It requires the `requests` and `json` packages to be installed.

To generate a new version, set the AMP_URL, AMP_USERNAME, and AMP_PASSWORD environment variables and run the script.

## Notes on missing methods

The generation script only uses the base ADS APISpec of an AMP Network Licence (my current licence). This means any Enterprise methods, methods added by plugins, or module-specific methods are not included. If you find yourself needing these methods frequently, please use the insance's API endpoint with the `ampapai_gen.py` script under `/utils`, then submit a pull request with the generated code.
If you need a method that is not included, you can use the `AMPAPI.APICall` method to run the method directly.
