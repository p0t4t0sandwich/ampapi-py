#!/bin/python3
# author: p0t4t0sandich
# description: A Python library for the AMP API

from ampapi.apimodules.MinecraftModule import MinecraftModule
from ampapi.modules.CommonAPI import CommonAPI

class Minecraft(CommonAPI):
    def __init__(self, baseUri: str, username: str = "", password: str = "", rememberMeToken: str = "", sessionId: str = ""):
        super().__init__(baseUri, username, password, rememberMeToken, sessionId)
        self.MinecraftModule = MinecraftModule(self)

    def Login(self) -> dict:
        """
        Simplified login function
        :returns: dict with the result of the login
        """
        loginResult: dict = super().Login()
        if "success" in loginResult.keys() and loginResult["success"] == True:
            self.rememberMeToken = loginResult["rememberMeToken"]
            self.sessionId = loginResult["sessionID"]

            # Update the session ID and remember me token of submodules
            self.MinecraftModule.sessionId = self.sessionId
            self.MinecraftModule.rememberMeToken = self.rememberMeToken

        return loginResult

    async def LoginAsync(self) -> dict:
        """
        Simplified login function
        :returns: dict with the result of the login
        """
        loginResult: dict = await super().LoginAsync()
        if "success" in loginResult.keys() and loginResult["success"] == True:
            self.rememberMeToken = loginResult["rememberMeToken"]
            self.sessionId = loginResult["sessionID"]

            # Update the session ID and remember me token of submodules
            self.MinecraftModule.sessionId = self.sessionId
            self.MinecraftModule.rememberMeToken = self.rememberMeToken

        return loginResult
