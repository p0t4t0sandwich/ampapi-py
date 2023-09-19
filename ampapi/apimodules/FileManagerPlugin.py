# An API that allows you to communicate with AMP installations from within Python
# Author: p0t4t0sandich

from typing import Any
from ampapi.ampapi import AMPAPI
from ampapi.types import *


class FileManagerPlugin(AMPAPI):
    def __init__(self, ampapi: AMPAPI) -> None:
        """Initializes the FileManagerPlugin class
        :param ampapi: The AMPAPI class to clone
        :returns: None
        """
        super().__init__(ampapi.baseUri, ampapi.username, ampapi.password, ampapi.rememberMeToken, ampapi.sessionId)

    def AppendFileChunk(self, Filename: str, Data: str, Delete: bool) -> Void:
        """
        Name Description Optional
        :param Filename: {str}  False
        :param Data: {str}  False
        :param Delete: {bool}  False
        :returns: Void
        """
        response: dict = self.api_call("FileManagerPlugin/AppendFileChunk", { 
            "Filename": Filename,
            "Data": Data,
            "Delete": Delete,
        })
        if response == None:
            response = {}
        return Void(**response)

    async def AppendFileChunkAsync(self, Filename: str, Data: str, Delete: bool) -> Void:
        """
        Name Description Optional
        :param Filename: {str}  False
        :param Data: {str}  False
        :param Delete: {bool}  False
        :returns: Void
        """
        response: dict = await self.api_call_async("FileManagerPlugin/AppendFileChunk", { 
            "Filename": Filename,
            "Data": Data,
            "Delete": Delete,
        })
        if response == None:
            response = {}
        return Void(**response)

    def CalculateFileMD5Sum(self, FilePath: str) -> ActionResult[str]:
        """
        Name Description Optional
        :param FilePath: {str}  False
        :returns: ActionResult[str]
        """
        response: dict = self.api_call("FileManagerPlugin/CalculateFileMD5Sum", { 
            "FilePath": FilePath,
        })
        return ActionResult[str](**response)

    async def CalculateFileMD5SumAsync(self, FilePath: str) -> ActionResult[str]:
        """
        Name Description Optional
        :param FilePath: {str}  False
        :returns: ActionResult[str]
        """
        response: dict = await self.api_call_async("FileManagerPlugin/CalculateFileMD5Sum", { 
            "FilePath": FilePath,
        })
        return ActionResult[str](**response)

    def ChangeExclusion(self, ModifyPath: str, AsDirectory: bool, Exclude: bool) -> ActionResult[Any]:
        """
        Name Description Optional
        :param ModifyPath: {str}  False
        :param AsDirectory: {bool}  False
        :param Exclude: {bool}  False
        :returns: ActionResult[Any]
        """
        response: dict = self.api_call("FileManagerPlugin/ChangeExclusion", { 
            "ModifyPath": ModifyPath,
            "AsDirectory": AsDirectory,
            "Exclude": Exclude,
        })
        return ActionResult[Any](**response)

    async def ChangeExclusionAsync(self, ModifyPath: str, AsDirectory: bool, Exclude: bool) -> ActionResult[Any]:
        """
        Name Description Optional
        :param ModifyPath: {str}  False
        :param AsDirectory: {bool}  False
        :param Exclude: {bool}  False
        :returns: ActionResult[Any]
        """
        response: dict = await self.api_call_async("FileManagerPlugin/ChangeExclusion", { 
            "ModifyPath": ModifyPath,
            "AsDirectory": AsDirectory,
            "Exclude": Exclude,
        })
        return ActionResult[Any](**response)

    def CopyFile(self, Origin: str, TargetDirectory: str) -> ActionResult[Any]:
        """
        Name Description Optional
        :param Origin: {str}  False
        :param TargetDirectory: {str}  False
        :returns: ActionResult[Any]
        """
        response: dict = self.api_call("FileManagerPlugin/CopyFile", { 
            "Origin": Origin,
            "TargetDirectory": TargetDirectory,
        })
        return ActionResult[Any](**response)

    async def CopyFileAsync(self, Origin: str, TargetDirectory: str) -> ActionResult[Any]:
        """
        Name Description Optional
        :param Origin: {str}  False
        :param TargetDirectory: {str}  False
        :returns: ActionResult[Any]
        """
        response: dict = await self.api_call_async("FileManagerPlugin/CopyFile", { 
            "Origin": Origin,
            "TargetDirectory": TargetDirectory,
        })
        return ActionResult[Any](**response)

    def CreateArchive(self, PathToArchive: str) -> ActionResult[Any]:
        """
        Name Description Optional
        :param PathToArchive: {str}  False
        :returns: ActionResult[Any]
        """
        response: dict = self.api_call("FileManagerPlugin/CreateArchive", { 
            "PathToArchive": PathToArchive,
        })
        return ActionResult[Any](**response)

    async def CreateArchiveAsync(self, PathToArchive: str) -> ActionResult[Any]:
        """
        Name Description Optional
        :param PathToArchive: {str}  False
        :returns: ActionResult[Any]
        """
        response: dict = await self.api_call_async("FileManagerPlugin/CreateArchive", { 
            "PathToArchive": PathToArchive,
        })
        return ActionResult[Any](**response)

    def CreateDirectory(self, NewPath: str) -> ActionResult[Any]:
        """
        Name Description Optional
        :param NewPath: {str}  False
        :returns: ActionResult[Any]
        """
        response: dict = self.api_call("FileManagerPlugin/CreateDirectory", { 
            "NewPath": NewPath,
        })
        return ActionResult[Any](**response)

    async def CreateDirectoryAsync(self, NewPath: str) -> ActionResult[Any]:
        """
        Name Description Optional
        :param NewPath: {str}  False
        :returns: ActionResult[Any]
        """
        response: dict = await self.api_call_async("FileManagerPlugin/CreateDirectory", { 
            "NewPath": NewPath,
        })
        return ActionResult[Any](**response)

    def DownloadFileFromURL(self, Source: URL, TargetDirectory: str) -> ActionResult[Any]:
        """
        Name Description Optional
        :param Source: {URL}  False
        :param TargetDirectory: {str}  False
        :returns: ActionResult[Any]
        """
        response: dict = self.api_call("FileManagerPlugin/DownloadFileFromURL", { 
            "Source": Source,
            "TargetDirectory": TargetDirectory,
        })
        return ActionResult[Any](**response)

    async def DownloadFileFromURLAsync(self, Source: URL, TargetDirectory: str) -> ActionResult[Any]:
        """
        Name Description Optional
        :param Source: {URL}  False
        :param TargetDirectory: {str}  False
        :returns: ActionResult[Any]
        """
        response: dict = await self.api_call_async("FileManagerPlugin/DownloadFileFromURL", { 
            "Source": Source,
            "TargetDirectory": TargetDirectory,
        })
        return ActionResult[Any](**response)

    def Dummy(self, ) -> Void:
        """
        Name Description Optional
        :returns: Void
        """
        response: dict = self.api_call("FileManagerPlugin/Dummy", { 
        })
        if response == None:
            response = {}
        return Void(**response)

    async def DummyAsync(self, ) -> Void:
        """
        Name Description Optional
        :returns: Void
        """
        response: dict = await self.api_call_async("FileManagerPlugin/Dummy", { 
        })
        if response == None:
            response = {}
        return Void(**response)

    def EmptyTrash(self, TrashDirectoryName: str) -> ActionResult[Any]:
        """
        Name Description Optional
        :param TrashDirectoryName: {str}  False
        :returns: ActionResult[Any]
        """
        response: dict = self.api_call("FileManagerPlugin/EmptyTrash", { 
            "TrashDirectoryName": TrashDirectoryName,
        })
        return ActionResult[Any](**response)

    async def EmptyTrashAsync(self, TrashDirectoryName: str) -> ActionResult[Any]:
        """
        Name Description Optional
        :param TrashDirectoryName: {str}  False
        :returns: ActionResult[Any]
        """
        response: dict = await self.api_call_async("FileManagerPlugin/EmptyTrash", { 
            "TrashDirectoryName": TrashDirectoryName,
        })
        return ActionResult[Any](**response)

    def ExtractArchive(self, ArchivePath: str, DestinationPath: str) -> ActionResult[Any]:
        """
        Name Description Optional
        :param ArchivePath: {str}  False
        :param DestinationPath: {str}  True
        :returns: ActionResult[Any]
        """
        response: dict = self.api_call("FileManagerPlugin/ExtractArchive", { 
            "ArchivePath": ArchivePath,
            "DestinationPath": DestinationPath,
        })
        return ActionResult[Any](**response)

    async def ExtractArchiveAsync(self, ArchivePath: str, DestinationPath: str) -> ActionResult[Any]:
        """
        Name Description Optional
        :param ArchivePath: {str}  False
        :param DestinationPath: {str}  True
        :returns: ActionResult[Any]
        """
        response: dict = await self.api_call_async("FileManagerPlugin/ExtractArchive", { 
            "ArchivePath": ArchivePath,
            "DestinationPath": DestinationPath,
        })
        return ActionResult[Any](**response)

    def GetDirectoryListing(self, Dir: str) -> list[dict]:
        """
        Name Description Optional
        :param Dir: {str}  False
        :returns: list[dict]
        """
        response: dict = self.api_call("FileManagerPlugin/GetDirectoryListing", { 
            "Dir": Dir,
        })
        return list[dict](**response)

    async def GetDirectoryListingAsync(self, Dir: str) -> list[dict]:
        """
        Name Description Optional
        :param Dir: {str}  False
        :returns: list[dict]
        """
        response: dict = await self.api_call_async("FileManagerPlugin/GetDirectoryListing", { 
            "Dir": Dir,
        })
        return list[dict](**response)

    def GetFileChunk(self, Filename: str, Position: int, Length: int) -> Any:
        """
        Name Description Optional
        :param Filename: {str}  False
        :param Position: {int}  False
        :param Length: {int}  False
        :returns: Any
        """
        response: dict = self.api_call("FileManagerPlugin/GetFileChunk", { 
            "Filename": Filename,
            "Position": Position,
            "Length": Length,
        })
        return Any(**response)

    async def GetFileChunkAsync(self, Filename: str, Position: int, Length: int) -> Any:
        """
        Name Description Optional
        :param Filename: {str}  False
        :param Position: {int}  False
        :param Length: {int}  False
        :returns: Any
        """
        response: dict = await self.api_call_async("FileManagerPlugin/GetFileChunk", { 
            "Filename": Filename,
            "Position": Position,
            "Length": Length,
        })
        return Any(**response)

    def ReadFileChunk(self, Filename: str, Offset: int, ChunkSize: int) -> ActionResult[str]:
        """
        Name Description Optional
        :param Filename: {str}  False
        :param Offset: {int}  False
        :param ChunkSize: {int}  True
        :returns: ActionResult[str]
        """
        response: dict = self.api_call("FileManagerPlugin/ReadFileChunk", { 
            "Filename": Filename,
            "Offset": Offset,
            "ChunkSize": ChunkSize,
        })
        return ActionResult[str](**response)

    async def ReadFileChunkAsync(self, Filename: str, Offset: int, ChunkSize: int) -> ActionResult[str]:
        """
        Name Description Optional
        :param Filename: {str}  False
        :param Offset: {int}  False
        :param ChunkSize: {int}  True
        :returns: ActionResult[str]
        """
        response: dict = await self.api_call_async("FileManagerPlugin/ReadFileChunk", { 
            "Filename": Filename,
            "Offset": Offset,
            "ChunkSize": ChunkSize,
        })
        return ActionResult[str](**response)

    def RenameDirectory(self, oldDirectory: str, NewDirectoryName: str) -> ActionResult[Any]:
        """The name component of the new directory (not the full path)
        Name Description Optional
        :param oldDirectory: {str} The full path to the old directory False
        :param NewDirectoryName: {str} The name component of the new directory (not the full path) False
        :returns: ActionResult[Any]
        """
        response: dict = self.api_call("FileManagerPlugin/RenameDirectory", { 
            "oldDirectory": oldDirectory,
            "NewDirectoryName": NewDirectoryName,
        })
        return ActionResult[Any](**response)

    async def RenameDirectoryAsync(self, oldDirectory: str, NewDirectoryName: str) -> ActionResult[Any]:
        """The name component of the new directory (not the full path)
        Name Description Optional
        :param oldDirectory: {str} The full path to the old directory False
        :param NewDirectoryName: {str} The name component of the new directory (not the full path) False
        :returns: ActionResult[Any]
        """
        response: dict = await self.api_call_async("FileManagerPlugin/RenameDirectory", { 
            "oldDirectory": oldDirectory,
            "NewDirectoryName": NewDirectoryName,
        })
        return ActionResult[Any](**response)

    def RenameFile(self, Filename: str, NewFilename: str) -> ActionResult[Any]:
        """
        Name Description Optional
        :param Filename: {str}  False
        :param NewFilename: {str}  False
        :returns: ActionResult[Any]
        """
        response: dict = self.api_call("FileManagerPlugin/RenameFile", { 
            "Filename": Filename,
            "NewFilename": NewFilename,
        })
        return ActionResult[Any](**response)

    async def RenameFileAsync(self, Filename: str, NewFilename: str) -> ActionResult[Any]:
        """
        Name Description Optional
        :param Filename: {str}  False
        :param NewFilename: {str}  False
        :returns: ActionResult[Any]
        """
        response: dict = await self.api_call_async("FileManagerPlugin/RenameFile", { 
            "Filename": Filename,
            "NewFilename": NewFilename,
        })
        return ActionResult[Any](**response)

    def TrashDirectory(self, DirectoryName: str) -> ActionResult[Any]:
        """
        Name Description Optional
        :param DirectoryName: {str}  False
        :returns: ActionResult[Any]
        """
        response: dict = self.api_call("FileManagerPlugin/TrashDirectory", { 
            "DirectoryName": DirectoryName,
        })
        return ActionResult[Any](**response)

    async def TrashDirectoryAsync(self, DirectoryName: str) -> ActionResult[Any]:
        """
        Name Description Optional
        :param DirectoryName: {str}  False
        :returns: ActionResult[Any]
        """
        response: dict = await self.api_call_async("FileManagerPlugin/TrashDirectory", { 
            "DirectoryName": DirectoryName,
        })
        return ActionResult[Any](**response)

    def TrashFile(self, Filename: str) -> ActionResult[Any]:
        """
        Name Description Optional
        :param Filename: {str}  False
        :returns: ActionResult[Any]
        """
        response: dict = self.api_call("FileManagerPlugin/TrashFile", { 
            "Filename": Filename,
        })
        return ActionResult[Any](**response)

    async def TrashFileAsync(self, Filename: str) -> ActionResult[Any]:
        """
        Name Description Optional
        :param Filename: {str}  False
        :returns: ActionResult[Any]
        """
        response: dict = await self.api_call_async("FileManagerPlugin/TrashFile", { 
            "Filename": Filename,
        })
        return ActionResult[Any](**response)

    def WriteFileChunk(self, Filename: str, Data: str, Offset: int, FinalChunk: bool) -> ActionResult[Any]:
        """
        Name Description Optional
        :param Filename: {str}  False
        :param Data: {str}  False
        :param Offset: {int}  False
        :param FinalChunk: {bool}  False
        :returns: ActionResult[Any]
        """
        response: dict = self.api_call("FileManagerPlugin/WriteFileChunk", { 
            "Filename": Filename,
            "Data": Data,
            "Offset": Offset,
            "FinalChunk": FinalChunk,
        })
        return ActionResult[Any](**response)

    async def WriteFileChunkAsync(self, Filename: str, Data: str, Offset: int, FinalChunk: bool) -> ActionResult[Any]:
        """
        Name Description Optional
        :param Filename: {str}  False
        :param Data: {str}  False
        :param Offset: {int}  False
        :param FinalChunk: {bool}  False
        :returns: ActionResult[Any]
        """
        response: dict = await self.api_call_async("FileManagerPlugin/WriteFileChunk", { 
            "Filename": Filename,
            "Data": Data,
            "Offset": Offset,
            "FinalChunk": FinalChunk,
        })
        return ActionResult[Any](**response)

