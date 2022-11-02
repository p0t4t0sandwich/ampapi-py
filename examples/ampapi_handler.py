import json
from ampapi.ampapi import AMPAPI
import requests


class AMPAPIHandler(AMPAPI):
    def __init__(self, baseUri: str, username: str, password: str = "", rememberMeToken: str = "", sessionId: str = "") -> None:
        super().__init__(baseUri=baseUri)
        self.username = username
        self.password = password
        self.rememberMeToken = rememberMeToken
        self.sessionId = sessionId

    def Login(self):
        loginResult = self.Core.Login(self.username, self.password, self.rememberMeToken, True)
        if "success" in loginResult.keys() and loginResult["success"]:
            self.rememberMeToken = loginResult["rememberMeToken"]
            self.sessionId = loginResult["sessionID"]
        return loginResult

    def initHandler(self):
        try:
            # Perform first-stage API initialization.
            APIInitOK = self.init()

            if not APIInitOK:
                print("API Init failed")
                return

            # The third parameter is either used for 2FA logins, or if no password is specified to use a remembered token from a previous login, or a service login token.
            loginResult = self.Login()

            if "success" in loginResult.keys() and loginResult["success"]:
                print("Login successful")

                # Perform second-stage API initialization, we only get the full API data once we're logged in.
                APIInitOK = self.init()
                if not APIInitOK:
                    print("API Stage 2 Init failed")
                    return
            else:
                print("Login failed")
                print(loginResult)

        except Exception as err:
            print(err)

    def APICallDirect(self, endpoint: str, data: dict = {}) -> dict:
        headers = {'accept': 'text/javascript',}
        session = {"SESSIONID": self.sessionId}
        data_added = dict(session, **data)

        data_json = json.dumps(data_added)

        res = requests.post(
            url=f'{self.dataSource}{endpoint}',
            headers=headers,
            data=data_json
        )
        res_json = json.loads(res.content)

        return res_json

    def InstanceAPICall(self, instance_id: str, endpoint: str, data: dict = {}) -> dict:
        result = self.APICallDirect(
            endpoint=f"/ADSModule/Servers/{instance_id}{endpoint}",
            data=data
        )
        return result

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
            return AMPAPIHandler(
                baseUri=self.baseUri + f"API/ADSModule/Servers/{instance_id}",
                username=self.username,
                password=self.password,
                rememberMeToken=loginResult["rememberMeToken"],
                sessionId=loginResult["sessionID"]
            )