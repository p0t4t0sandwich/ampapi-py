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