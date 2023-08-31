#!/bin/python3
# author: p0t4t0sandich
# description: A Python library for the AMP API

from typing import Any
from ampapi.ampapi import AMPAPI


class steamcmdplugin(AMPAPI):
    def __init__(self, ampapi: AMPAPI) -> None:
        """Initializes the steamcmdplugin class
        :param ampapi: The AMPAPI class to clone
        :returns: None
        """
        super().__init__(ampapi.baseUri, ampapi.username, ampapi.password, ampapi.rememberMeToken, ampapi.sessionId)

    def CancelSteamGuard(self, ) -> None:
        """
        Name Description Optional
        :returns: None
        """
        return self.api_call("steamcmdplugin/CancelSteamGuard", { 
        })

    async def CancelSteamGuardAsync(self, ) -> None:
        """
        Name Description Optional
        :returns: None
        """
        return await self.api_call_async("steamcmdplugin/CancelSteamGuard", { 
        })

    def SteamGuardCode(self, code: str) -> None:
        """
        Name Description Optional
        :param code: {str}  False
        :returns: None
        """
        return self.api_call("steamcmdplugin/SteamGuardCode", { 
            "code": code,
        })

    async def SteamGuardCodeAsync(self, code: str) -> None:
        """
        Name Description Optional
        :param code: {str}  False
        :returns: None
        """
        return await self.api_call_async("steamcmdplugin/SteamGuardCode", { 
            "code": code,
        })

    def SteamUsernamePassword(self, username: str, password: str) -> None:
        """
        Name Description Optional
        :param username: {str}  False
        :param password: {str}  False
        :returns: None
        """
        return self.api_call("steamcmdplugin/SteamUsernamePassword", { 
            "username": username,
            "password": password,
        })

    async def SteamUsernamePasswordAsync(self, username: str, password: str) -> None:
        """
        Name Description Optional
        :param username: {str}  False
        :param password: {str}  False
        :returns: None
        """
        return await self.api_call_async("steamcmdplugin/SteamUsernamePassword", { 
            "username": username,
            "password": password,
        })

