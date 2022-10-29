# ampapi-python

## This implementation is under active development, please feel free to contribute or create an issue if you've found anything that needs fixing

This API allows you to communicate with AMP installations from within Python.

Documentation for available API calls can be found by appending /API to the URL of any existing AMP installation.

Please Note: This program is directly based on the [ampapi-node](https://github.com/CubeCoders/ampapi-node) implementation and is almost verbatim in most aspects.

## Installation

```bash
pip install ampapi
```

or

```bash
pip install 'ampapi @ git+https://github.com/p0t4t0sandwich/ampapi-python.git'
```

## Async Example

```python
import asyncio
from ampapi.ampapi_async import AMPAPIAsync

async def start() -> None:
    API = AMPAPIAsync("http://localhost:8080/")

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
from ampapi import AMPAPI

def start() -> None:
    API = AMPAPI("http://localhost:8080/")

    try:
        # Perform first-stage API initialization.
        APIInitOK = API.init()

        if not APIInitOK:
            print("API Init failed")
            return

        # The third parameter is either used for 2FA logins, or if no password is specified to use a remembered token from a previous login, or a service login token.
        loginResult = API.Core.Login("admin", "myfancypassword123", "", False)

        if "success" in loginResult.keys() and loginResult["success"]:
            print("Login successful")
            API.sessionId = loginResult["sessionID"]

            # Perform second-stage API initialization, we only get the full API data once we're logged in.
            APIInitOK = API.init()
            if not APIInitOK:
                print("API Stage 2 Init failed")
                return

            # API call parameters are simply in the same order as shown in the documentation.
            API.Core.SendConsoleMessage("say Hello Everyone, this message was sent from the Python API!")
            currentStatus = API.Core.GetStatus()
            CPUUsagePercent = currentStatus["Metrics"]["CPU Usage"]["Percent"]
            print(f"Current CPU usage is: {CPUUsagePercent}%")

        else:
            print("Login failed")
            print(loginResult)

    except Exception as err:
        print(err)

start()
```

## Additional Notes

As you may have noticed, the async and non-async implementations differ quite a bit. This is due to lambda functions within python being unable to use async methods. Usually this can be solved by manually defining the function, but as that would be cumbersome, I've opted to create a script to grab the API spec from the AMP API and generate all the needed functions (script found under /utils/ampapi_async_gen.py).

Async implementation: `API.Core_LoginAsync()`

Sync implementation: `API.Core.Login()`

Additonally, unlike other languages, the "Zen of Python" prevents dot/property notation for dictionaries (Think API.Core.Login). I've used dataclasses and some class properties to bypass this, so in the end:

`API.Core.Login() == API["Core"]["Login"]()`.
