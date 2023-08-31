#!/bin/python3
# author: p0t4t0sandich
# description: A Python library for the AMP API

from typing import Any
from ampapi.ampapi import AMPAPI


class LocalFileBackupPlugin(AMPAPI):
    def __init__(self, ampapi: AMPAPI) -> None:
        """Initializes the LocalFileBackupPlugin class
        :param ampapi: The AMPAPI class to clone
        :returns: None
        """
        super().__init__(ampapi.baseUri, ampapi.username, ampapi.password, ampapi.rememberMeToken, ampapi.sessionId)

    def DeleteFromS3(self, BackupId: str) -> Any:
        """
        Name Description Optional
        :param BackupId: {str}  False
        :returns: Any
        """
        return self.api_call("LocalFileBackupPlugin/DeleteFromS3", { 
            "BackupId": BackupId,
        })

    async def DeleteFromS3Async(self, BackupId: str) -> Any:
        """
        Name Description Optional
        :param BackupId: {str}  False
        :returns: Any
        """
        return await self.api_call_async("LocalFileBackupPlugin/DeleteFromS3", { 
            "BackupId": BackupId,
        })

    def DeleteLocalBackup(self, BackupId: str) -> None:
        """
        Name Description Optional
        :param BackupId: {str}  False
        :returns: None
        """
        return self.api_call("LocalFileBackupPlugin/DeleteLocalBackup", { 
            "BackupId": BackupId,
        })

    async def DeleteLocalBackupAsync(self, BackupId: str) -> None:
        """
        Name Description Optional
        :param BackupId: {str}  False
        :returns: None
        """
        return await self.api_call_async("LocalFileBackupPlugin/DeleteLocalBackup", { 
            "BackupId": BackupId,
        })

    def DownloadFromS3(self, BackupId: str) -> Any:
        """
        Name Description Optional
        :param BackupId: {str}  False
        :returns: Any
        """
        return self.api_call("LocalFileBackupPlugin/DownloadFromS3", { 
            "BackupId": BackupId,
        })

    async def DownloadFromS3Async(self, BackupId: str) -> Any:
        """
        Name Description Optional
        :param BackupId: {str}  False
        :returns: Any
        """
        return await self.api_call_async("LocalFileBackupPlugin/DownloadFromS3", { 
            "BackupId": BackupId,
        })

    def GetBackups(self, ) -> list[dict]:
        """
        Name Description Optional
        :returns: list[dict]
        """
        return self.api_call("LocalFileBackupPlugin/GetBackups", { 
        })

    async def GetBackupsAsync(self, ) -> list[dict]:
        """
        Name Description Optional
        :returns: list[dict]
        """
        return await self.api_call_async("LocalFileBackupPlugin/GetBackups", { 
        })

    def RestoreBackup(self, BackupId: str, DeleteExistingData: bool) -> Any:
        """
        Name Description Optional
        :param BackupId: {str}  False
        :param DeleteExistingData: {bool}  True
        :returns: Any
        """
        return self.api_call("LocalFileBackupPlugin/RestoreBackup", { 
            "BackupId": BackupId,
            "DeleteExistingData": DeleteExistingData,
        })

    async def RestoreBackupAsync(self, BackupId: str, DeleteExistingData: bool) -> Any:
        """
        Name Description Optional
        :param BackupId: {str}  False
        :param DeleteExistingData: {bool}  True
        :returns: Any
        """
        return await self.api_call_async("LocalFileBackupPlugin/RestoreBackup", { 
            "BackupId": BackupId,
            "DeleteExistingData": DeleteExistingData,
        })

    def SetBackupSticky(self, BackupId: str, Sticky: bool) -> None:
        """
        Name Description Optional
        :param BackupId: {str}  False
        :param Sticky: {bool}  False
        :returns: None
        """
        return self.api_call("LocalFileBackupPlugin/SetBackupSticky", { 
            "BackupId": BackupId,
            "Sticky": Sticky,
        })

    async def SetBackupStickyAsync(self, BackupId: str, Sticky: bool) -> None:
        """
        Name Description Optional
        :param BackupId: {str}  False
        :param Sticky: {bool}  False
        :returns: None
        """
        return await self.api_call_async("LocalFileBackupPlugin/SetBackupSticky", { 
            "BackupId": BackupId,
            "Sticky": Sticky,
        })

    def TakeBackup(self, Title: str, Description: str, Sticky: bool) -> Any:
        """
        Name Description Optional
        :param Title: {str}  False
        :param Description: {str}  False
        :param Sticky: {bool}  False
        :returns: Any
        """
        return self.api_call("LocalFileBackupPlugin/TakeBackup", { 
            "Title": Title,
            "Description": Description,
            "Sticky": Sticky,
        })

    async def TakeBackupAsync(self, Title: str, Description: str, Sticky: bool) -> Any:
        """
        Name Description Optional
        :param Title: {str}  False
        :param Description: {str}  False
        :param Sticky: {bool}  False
        :returns: Any
        """
        return await self.api_call_async("LocalFileBackupPlugin/TakeBackup", { 
            "Title": Title,
            "Description": Description,
            "Sticky": Sticky,
        })

    def UploadToS3(self, BackupId: str) -> Any:
        """
        Name Description Optional
        :param BackupId: {str}  False
        :returns: Any
        """
        return self.api_call("LocalFileBackupPlugin/UploadToS3", { 
            "BackupId": BackupId,
        })

    async def UploadToS3Async(self, BackupId: str) -> Any:
        """
        Name Description Optional
        :param BackupId: {str}  False
        :returns: Any
        """
        return await self.api_call_async("LocalFileBackupPlugin/UploadToS3", { 
            "BackupId": BackupId,
        })

