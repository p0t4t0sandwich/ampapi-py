#!/bin/python3
# author: p0t4t0sandich
# description: A Python library for the AMP API

from typing import Any
from ampapi.ampapi import AMPAPI


class MinecraftModule(AMPAPI):
    def __init__(self, ampapi: AMPAPI) -> None:
        """Initializes the MinecraftModule class
        :param ampapi: The AMPAPI class to clone
        :returns: None
        """
        super().__init__(ampapi.baseUri, ampapi.username, ampapi.password, ampapi.rememberMeToken, ampapi.sessionId)

    def AcceptEULA(self, ) -> bool:
        """
        Name Description Optional
        :returns: bool
        """
        return self.api_call("MinecraftModule/AcceptEULA", { 
        })

    async def AcceptEULAAsync(self, ) -> bool:
        """
        Name Description Optional
        :returns: bool
        """
        return await self.api_call_async("MinecraftModule/AcceptEULA", { 
        })

    def AddOPEntry(self, UserOrUUID: str) -> Any:
        """
        Name Description Optional
        :param UserOrUUID: {str}  False
        :returns: Any
        """
        return self.api_call("MinecraftModule/AddOPEntry", { 
            "UserOrUUID": UserOrUUID,
        })

    async def AddOPEntryAsync(self, UserOrUUID: str) -> Any:
        """
        Name Description Optional
        :param UserOrUUID: {str}  False
        :returns: Any
        """
        return await self.api_call_async("MinecraftModule/AddOPEntry", { 
            "UserOrUUID": UserOrUUID,
        })

    def AddToWhitelist(self, UserOrUUID: str) -> Any:
        """
        Name Description Optional
        :param UserOrUUID: {str}  False
        :returns: Any
        """
        return self.api_call("MinecraftModule/AddToWhitelist", { 
            "UserOrUUID": UserOrUUID,
        })

    async def AddToWhitelistAsync(self, UserOrUUID: str) -> Any:
        """
        Name Description Optional
        :param UserOrUUID: {str}  False
        :returns: Any
        """
        return await self.api_call_async("MinecraftModule/AddToWhitelist", { 
            "UserOrUUID": UserOrUUID,
        })

    def BanUserByID(self, ID: str) -> None:
        """
        Name Description Optional
        :param ID: {str}  False
        :returns: None
        """
        return self.api_call("MinecraftModule/BanUserByID", { 
            "ID": ID,
        })

    async def BanUserByIDAsync(self, ID: str) -> None:
        """
        Name Description Optional
        :param ID: {str}  False
        :returns: None
        """
        return await self.api_call_async("MinecraftModule/BanUserByID", { 
            "ID": ID,
        })

    def BukGetCategories(self, ) -> dict:
        """
        Name Description Optional
        :returns: dict
        """
        return self.api_call("MinecraftModule/BukGetCategories", { 
        })

    async def BukGetCategoriesAsync(self, ) -> dict:
        """
        Name Description Optional
        :returns: dict
        """
        return await self.api_call_async("MinecraftModule/BukGetCategories", { 
        })

    def BukGetInstallUpdatePlugin(self, pluginId: int) -> Any:
        """
        Name Description Optional
        :param pluginId: {int}  False
        :returns: Any
        """
        return self.api_call("MinecraftModule/BukGetInstallUpdatePlugin", { 
            "pluginId": pluginId,
        })

    async def BukGetInstallUpdatePluginAsync(self, pluginId: int) -> Any:
        """
        Name Description Optional
        :param pluginId: {int}  False
        :returns: Any
        """
        return await self.api_call_async("MinecraftModule/BukGetInstallUpdatePlugin", { 
            "pluginId": pluginId,
        })

    def BukGetInstalledPlugins(self, ) -> dict:
        """
        Name Description Optional
        :returns: dict
        """
        return self.api_call("MinecraftModule/BukGetInstalledPlugins", { 
        })

    async def BukGetInstalledPluginsAsync(self, ) -> dict:
        """
        Name Description Optional
        :returns: dict
        """
        return await self.api_call_async("MinecraftModule/BukGetInstalledPlugins", { 
        })

    def BukGetPluginInfo(self, PluginId: int) -> dict:
        """
        Name Description Optional
        :param PluginId: {int}  False
        :returns: dict
        """
        return self.api_call("MinecraftModule/BukGetPluginInfo", { 
            "PluginId": PluginId,
        })

    async def BukGetPluginInfoAsync(self, PluginId: int) -> dict:
        """
        Name Description Optional
        :param PluginId: {int}  False
        :returns: dict
        """
        return await self.api_call_async("MinecraftModule/BukGetPluginInfo", { 
            "PluginId": PluginId,
        })

    def BukGetPluginsForCategory(self, CategoryId: str, PageNumber: int, PageSize: int) -> dict:
        """
        Name Description Optional
        :param CategoryId: {str}  False
        :param PageNumber: {int}  False
        :param PageSize: {int}  False
        :returns: dict
        """
        return self.api_call("MinecraftModule/BukGetPluginsForCategory", { 
            "CategoryId": CategoryId,
            "PageNumber": PageNumber,
            "PageSize": PageSize,
        })

    async def BukGetPluginsForCategoryAsync(self, CategoryId: str, PageNumber: int, PageSize: int) -> dict:
        """
        Name Description Optional
        :param CategoryId: {str}  False
        :param PageNumber: {int}  False
        :param PageSize: {int}  False
        :returns: dict
        """
        return await self.api_call_async("MinecraftModule/BukGetPluginsForCategory", { 
            "CategoryId": CategoryId,
            "PageNumber": PageNumber,
            "PageSize": PageSize,
        })

    def BukGetPopularPlugins(self, ) -> dict:
        """
        Name Description Optional
        :returns: dict
        """
        return self.api_call("MinecraftModule/BukGetPopularPlugins", { 
        })

    async def BukGetPopularPluginsAsync(self, ) -> dict:
        """
        Name Description Optional
        :returns: dict
        """
        return await self.api_call_async("MinecraftModule/BukGetPopularPlugins", { 
        })

    def BukGetRemovePlugin(self, PluginId: int) -> None:
        """
        Name Description Optional
        :param PluginId: {int}  False
        :returns: None
        """
        return self.api_call("MinecraftModule/BukGetRemovePlugin", { 
            "PluginId": PluginId,
        })

    async def BukGetRemovePluginAsync(self, PluginId: int) -> None:
        """
        Name Description Optional
        :param PluginId: {int}  False
        :returns: None
        """
        return await self.api_call_async("MinecraftModule/BukGetRemovePlugin", { 
            "PluginId": PluginId,
        })

    def BukGetSearch(self, Query: str, PageNumber: int, PageSize: int) -> dict:
        """
        Name Description Optional
        :param Query: {str}  False
        :param PageNumber: {int}  False
        :param PageSize: {int}  False
        :returns: dict
        """
        return self.api_call("MinecraftModule/BukGetSearch", { 
            "Query": Query,
            "PageNumber": PageNumber,
            "PageSize": PageSize,
        })

    async def BukGetSearchAsync(self, Query: str, PageNumber: int, PageSize: int) -> dict:
        """
        Name Description Optional
        :param Query: {str}  False
        :param PageNumber: {int}  False
        :param PageSize: {int}  False
        :returns: dict
        """
        return await self.api_call_async("MinecraftModule/BukGetSearch", { 
            "Query": Query,
            "PageNumber": PageNumber,
            "PageSize": PageSize,
        })

    def ClearInventoryByID(self, ID: str) -> None:
        """
        Name Description Optional
        :param ID: {str}  False
        :returns: None
        """
        return self.api_call("MinecraftModule/ClearInventoryByID", { 
            "ID": ID,
        })

    async def ClearInventoryByIDAsync(self, ID: str) -> None:
        """
        Name Description Optional
        :param ID: {str}  False
        :returns: None
        """
        return await self.api_call_async("MinecraftModule/ClearInventoryByID", { 
            "ID": ID,
        })

    def GetFailureReason(self, ) -> str:
        """
        Name Description Optional
        :returns: str
        """
        return self.api_call("MinecraftModule/GetFailureReason", { 
        })

    async def GetFailureReasonAsync(self, ) -> str:
        """
        Name Description Optional
        :returns: str
        """
        return await self.api_call_async("MinecraftModule/GetFailureReason", { 
        })

    def GetHeadByUUID(self, id: str) -> str:
        """
        Name Description Optional
        :param id: {str}  False
        :returns: str
        """
        return self.api_call("MinecraftModule/GetHeadByUUID", { 
            "id": id,
        })

    async def GetHeadByUUIDAsync(self, id: str) -> str:
        """
        Name Description Optional
        :param id: {str}  False
        :returns: str
        """
        return await self.api_call_async("MinecraftModule/GetHeadByUUID", { 
            "id": id,
        })

    def GetOPWhitelist(self, ) -> dict:
        """
        Name Description Optional
        :returns: dict
        """
        return self.api_call("MinecraftModule/GetOPWhitelist", { 
        })

    async def GetOPWhitelistAsync(self, ) -> dict:
        """
        Name Description Optional
        :returns: dict
        """
        return await self.api_call_async("MinecraftModule/GetOPWhitelist", { 
        })

    def GetWhitelist(self, ) -> list[dict]:
        """
        Name Description Optional
        :returns: list[dict]
        """
        return self.api_call("MinecraftModule/GetWhitelist", { 
        })

    async def GetWhitelistAsync(self, ) -> list[dict]:
        """
        Name Description Optional
        :returns: list[dict]
        """
        return await self.api_call_async("MinecraftModule/GetWhitelist", { 
        })

    def KickUserByID(self, ID: str) -> None:
        """
        Name Description Optional
        :param ID: {str}  False
        :returns: None
        """
        return self.api_call("MinecraftModule/KickUserByID", { 
            "ID": ID,
        })

    async def KickUserByIDAsync(self, ID: str) -> None:
        """
        Name Description Optional
        :param ID: {str}  False
        :returns: None
        """
        return await self.api_call_async("MinecraftModule/KickUserByID", { 
            "ID": ID,
        })

    def KillByID(self, ID: str) -> None:
        """
        Name Description Optional
        :param ID: {str}  False
        :returns: None
        """
        return self.api_call("MinecraftModule/KillByID", { 
            "ID": ID,
        })

    async def KillByIDAsync(self, ID: str) -> None:
        """
        Name Description Optional
        :param ID: {str}  False
        :returns: None
        """
        return await self.api_call_async("MinecraftModule/KillByID", { 
            "ID": ID,
        })

    def LoadOPList(self, ) -> list[dict]:
        """
        Name Description Optional
        :returns: list[dict]
        """
        return self.api_call("MinecraftModule/LoadOPList", { 
        })

    async def LoadOPListAsync(self, ) -> list[dict]:
        """
        Name Description Optional
        :returns: list[dict]
        """
        return await self.api_call_async("MinecraftModule/LoadOPList", { 
        })

    def RemoveOPEntry(self, UserOrUUID: str) -> None:
        """
        Name Description Optional
        :param UserOrUUID: {str}  False
        :returns: None
        """
        return self.api_call("MinecraftModule/RemoveOPEntry", { 
            "UserOrUUID": UserOrUUID,
        })

    async def RemoveOPEntryAsync(self, UserOrUUID: str) -> None:
        """
        Name Description Optional
        :param UserOrUUID: {str}  False
        :returns: None
        """
        return await self.api_call_async("MinecraftModule/RemoveOPEntry", { 
            "UserOrUUID": UserOrUUID,
        })

    def RemoveWhitelistEntry(self, UserOrUUID: str) -> None:
        """
        Name Description Optional
        :param UserOrUUID: {str}  False
        :returns: None
        """
        return self.api_call("MinecraftModule/RemoveWhitelistEntry", { 
            "UserOrUUID": UserOrUUID,
        })

    async def RemoveWhitelistEntryAsync(self, UserOrUUID: str) -> None:
        """
        Name Description Optional
        :param UserOrUUID: {str}  False
        :returns: None
        """
        return await self.api_call_async("MinecraftModule/RemoveWhitelistEntry", { 
            "UserOrUUID": UserOrUUID,
        })

    def SmiteByID(self, ID: str) -> None:
        """
        Name Description Optional
        :param ID: {str}  False
        :returns: None
        """
        return self.api_call("MinecraftModule/SmiteByID", { 
            "ID": ID,
        })

    async def SmiteByIDAsync(self, ID: str) -> None:
        """
        Name Description Optional
        :param ID: {str}  False
        :returns: None
        """
        return await self.api_call_async("MinecraftModule/SmiteByID", { 
            "ID": ID,
        })

