from ampapi.ampapi_old import AMPAPI

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