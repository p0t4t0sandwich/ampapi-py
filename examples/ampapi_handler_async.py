from ampapi.ampapi_async import AMPAPIAsync


class AMPAPIHandlerAsync(AMPAPIAsync):
    def __init__(self, baseUri: str, username: str, password: str = "", rememberMeToken: str = "", sessionId: str = "") -> None:
        super().__init__(baseUri=baseUri)
        self.username = username
        self.password = password
        self.rememberMeToken = rememberMeToken
        self.sessionId = sessionId

    async def LoginAsync(self):
        loginResult = await self.Core_LoginAsync(self.username, self.password, self.rememberMeToken, True)
        if "success" in loginResult.keys() and loginResult["success"]:
            self.rememberMeToken = loginResult["rememberMeToken"]
            self.sessionId = loginResult["sessionID"]
        return loginResult

    async def InstanceAPICallAsync(self, instance_id: str, endpoint: str, data: dict = {}) -> dict:
        result = await self.APICallAsync(
            endpoint=f"/ADSModule/Servers/{instance_id}{endpoint}",
            data=data
        )
        return result

    async def InstanceLoginAsync(self, instance_id: str):
        loginResult = await self.InstanceAPICallAsync(
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
            return AMPAPIHandlerAsync(
                baseUri=self.baseUri + f"API/ADSModule/Servers/{instance_id}",
                username=self.username,
                rememberMeToken=loginResult["rememberMeToken"],
                sessionId=loginResult["sessionID"]
            )
