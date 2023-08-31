#!/bin/python3
# author: p0t4t0sandich
# description: A Python library for the AMP API

from typing import Any
from ampapi.ampapi import AMPAPI


class FileManagerPlugin(AMPAPI):
    def __init__(self, ampapi: AMPAPI) -> None:
        """Initializes the FileManagerPlugin class
        :param ampapi: The AMPAPI class to clone
        :returns: None
        """
        super().__init__(ampapi.baseUri, ampapi.username, ampapi.password, ampapi.rememberMeToken, ampapi.sessionId)

    def AppendFileChunk(self, Filename: str, Data: str, Delete: bool) -> None:
        """
        Name Description Optional
        :param Filename: {str}  False
        :param Data: {str}  False
        :param Delete: {bool}  False
        :returns: None
        """
        return self.api_call("FileManagerPlugin/AppendFileChunk", { 
            "Filename": Filename,
            "Data": Data,
            "Delete": Delete,
        })

    async def AppendFileChunkAsync(self, Filename: str, Data: str, Delete: bool) -> None:
        """
        Name Description Optional
        :param Filename: {str}  False
        :param Data: {str}  False
        :param Delete: {bool}  False
        :returns: None
        """
        return await self.api_call_async("FileManagerPlugin/AppendFileChunk", { 
            "Filename": Filename,
            "Data": Data,
            "Delete": Delete,
        })

    def CalculateFileMD5Sum(self, FilePath: str) -> Any:
        """
        Name Description Optional
        :param FilePath: {str}  False
        :returns: Any
        """
        return self.api_call("FileManagerPlugin/CalculateFileMD5Sum", { 
            "FilePath": FilePath,
        })

    async def CalculateFileMD5SumAsync(self, FilePath: str) -> Any:
        """
        Name Description Optional
        :param FilePath: {str}  False
        :returns: Any
        """
        return await self.api_call_async("FileManagerPlugin/CalculateFileMD5Sum", { 
            "FilePath": FilePath,
        })

    def ChangeExclusion(self, ModifyPath: str, AsDirectory: bool, Exclude: bool) -> Any:
        """
        Name Description Optional
        :param ModifyPath: {str}  False
        :param AsDirectory: {bool}  False
        :param Exclude: {bool}  False
        :returns: Any
        """
        return self.api_call("FileManagerPlugin/ChangeExclusion", { 
            "ModifyPath": ModifyPath,
            "AsDirectory": AsDirectory,
            "Exclude": Exclude,
        })

    async def ChangeExclusionAsync(self, ModifyPath: str, AsDirectory: bool, Exclude: bool) -> Any:
        """
        Name Description Optional
        :param ModifyPath: {str}  False
        :param AsDirectory: {bool}  False
        :param Exclude: {bool}  False
        :returns: Any
        """
        return await self.api_call_async("FileManagerPlugin/ChangeExclusion", { 
            "ModifyPath": ModifyPath,
            "AsDirectory": AsDirectory,
            "Exclude": Exclude,
        })

    def CopyFile(self, Origin: str, TargetDirectory: str) -> Any:
        """
        Name Description Optional
        :param Origin: {str}  False
        :param TargetDirectory: {str}  False
        :returns: Any
        """
        return self.api_call("FileManagerPlugin/CopyFile", { 
            "Origin": Origin,
            "TargetDirectory": TargetDirectory,
        })

    async def CopyFileAsync(self, Origin: str, TargetDirectory: str) -> Any:
        """
        Name Description Optional
        :param Origin: {str}  False
        :param TargetDirectory: {str}  False
        :returns: Any
        """
        return await self.api_call_async("FileManagerPlugin/CopyFile", { 
            "Origin": Origin,
            "TargetDirectory": TargetDirectory,
        })

    def CreateArchive(self, PathToArchive: str) -> Any:
        """
        Name Description Optional
        :param PathToArchive: {str}  False
        :returns: Any
        """
        return self.api_call("FileManagerPlugin/CreateArchive", { 
            "PathToArchive": PathToArchive,
        })

    async def CreateArchiveAsync(self, PathToArchive: str) -> Any:
        """
        Name Description Optional
        :param PathToArchive: {str}  False
        :returns: Any
        """
        return await self.api_call_async("FileManagerPlugin/CreateArchive", { 
            "PathToArchive": PathToArchive,
        })

    def CreateDirectory(self, NewPath: str) -> Any:
        """
        Name Description Optional
        :param NewPath: {str}  False
        :returns: Any
        """
        return self.api_call("FileManagerPlugin/CreateDirectory", { 
            "NewPath": NewPath,
        })

    async def CreateDirectoryAsync(self, NewPath: str) -> Any:
        """
        Name Description Optional
        :param NewPath: {str}  False
        :returns: Any
        """
        return await self.api_call_async("FileManagerPlugin/CreateDirectory", { 
            "NewPath": NewPath,
        })

    def DownloadFileFromURL(self, Source: str, TargetDirectory: str) -> Any:
        """
        Name Description Optional
        :param Source: {str}  False
        :param TargetDirectory: {str}  False
        :returns: Any
        """
        return self.api_call("FileManagerPlugin/DownloadFileFromURL", { 
            "Source": Source,
            "TargetDirectory": TargetDirectory,
        })

    async def DownloadFileFromURLAsync(self, Source: str, TargetDirectory: str) -> Any:
        """
        Name Description Optional
        :param Source: {str}  False
        :param TargetDirectory: {str}  False
        :returns: Any
        """
        return await self.api_call_async("FileManagerPlugin/DownloadFileFromURL", { 
            "Source": Source,
            "TargetDirectory": TargetDirectory,
        })

    def Dummy(self, ) -> None:
        """
        Name Description Optional
        :returns: None
        """
        return self.api_call("FileManagerPlugin/Dummy", { 
        })

    async def DummyAsync(self, ) -> None:
        """
        Name Description Optional
        :returns: None
        """
        return await self.api_call_async("FileManagerPlugin/Dummy", { 
        })

    def EmptyTrash(self, TrashDirectoryName: str) -> Any:
        """
        Name Description Optional
        :param TrashDirectoryName: {str}  False
        :returns: Any
        """
        return self.api_call("FileManagerPlugin/EmptyTrash", { 
            "TrashDirectoryName": TrashDirectoryName,
        })

    async def EmptyTrashAsync(self, TrashDirectoryName: str) -> Any:
        """
        Name Description Optional
        :param TrashDirectoryName: {str}  False
        :returns: Any
        """
        return await self.api_call_async("FileManagerPlugin/EmptyTrash", { 
            "TrashDirectoryName": TrashDirectoryName,
        })

    def ExtractArchive(self, ArchivePath: str, DestinationPath: str) -> Any:
        """
        Name Description Optional
        :param ArchivePath: {str}  False
        :param DestinationPath: {str}  True
        :returns: Any
        """
        return self.api_call("FileManagerPlugin/ExtractArchive", { 
            "ArchivePath": ArchivePath,
            "DestinationPath": DestinationPath,
        })

    async def ExtractArchiveAsync(self, ArchivePath: str, DestinationPath: str) -> Any:
        """
        Name Description Optional
        :param ArchivePath: {str}  False
        :param DestinationPath: {str}  True
        :returns: Any
        """
        return await self.api_call_async("FileManagerPlugin/ExtractArchive", { 
            "ArchivePath": ArchivePath,
            "DestinationPath": DestinationPath,
        })

    def GetDirectoryListing(self, Dir: str) -> list[dict]:
        """
        Name Description Optional
        :param Dir: {str}  False
        :returns: list[dict]
        """
        return self.api_call("FileManagerPlugin/GetDirectoryListing", { 
            "Dir": Dir,
        })

    async def GetDirectoryListingAsync(self, Dir: str) -> list[dict]:
        """
        Name Description Optional
        :param Dir: {str}  False
        :returns: list[dict]
        """
        return await self.api_call_async("FileManagerPlugin/GetDirectoryListing", { 
            "Dir": Dir,
        })

    def GetFileChunk(self, Filename: str, Position: int, Length: int) -> Any:
        """
        Name Description Optional
        :param Filename: {str}  False
        :param Position: {int}  False
        :param Length: {int}  False
        :returns: Any
        """
        return self.api_call("FileManagerPlugin/GetFileChunk", { 
            "Filename": Filename,
            "Position": Position,
            "Length": Length,
        })

    async def GetFileChunkAsync(self, Filename: str, Position: int, Length: int) -> Any:
        """
        Name Description Optional
        :param Filename: {str}  False
        :param Position: {int}  False
        :param Length: {int}  False
        :returns: Any
        """
        return await self.api_call_async("FileManagerPlugin/GetFileChunk", { 
            "Filename": Filename,
            "Position": Position,
            "Length": Length,
        })

    def ReadFileChunk(self, Filename: str, Offset: int, ChunkSize: int) -> Any:
        """
        Name Description Optional
        :param Filename: {str}  False
        :param Offset: {int}  False
        :param ChunkSize: {int}  True
        :returns: Any
        """
        return self.api_call("FileManagerPlugin/ReadFileChunk", { 
            "Filename": Filename,
            "Offset": Offset,
            "ChunkSize": ChunkSize,
        })

    async def ReadFileChunkAsync(self, Filename: str, Offset: int, ChunkSize: int) -> Any:
        """
        Name Description Optional
        :param Filename: {str}  False
        :param Offset: {int}  False
        :param ChunkSize: {int}  True
        :returns: Any
        """
        return await self.api_call_async("FileManagerPlugin/ReadFileChunk", { 
            "Filename": Filename,
            "Offset": Offset,
            "ChunkSize": ChunkSize,
        })

    def RenameDirectory(self, oldDirectory: str, NewDirectoryName: str) -> Any:
        """The name component of the new directory (not the full path)
        Name Description Optional
        :param oldDirectory: {str} The full path to the old directory False
        :param NewDirectoryName: {str} The name component of the new directory (not the full path) False
        :returns: Any
        """
        return self.api_call("FileManagerPlugin/RenameDirectory", { 
            "oldDirectory": oldDirectory,
            "NewDirectoryName": NewDirectoryName,
        })

    async def RenameDirectoryAsync(self, oldDirectory: str, NewDirectoryName: str) -> Any:
        """The name component of the new directory (not the full path)
        Name Description Optional
        :param oldDirectory: {str} The full path to the old directory False
        :param NewDirectoryName: {str} The name component of the new directory (not the full path) False
        :returns: Any
        """
        return await self.api_call_async("FileManagerPlugin/RenameDirectory", { 
            "oldDirectory": oldDirectory,
            "NewDirectoryName": NewDirectoryName,
        })

    def RenameFile(self, Filename: str, NewFilename: str) -> Any:
        """
        Name Description Optional
        :param Filename: {str}  False
        :param NewFilename: {str}  False
        :returns: Any
        """
        return self.api_call("FileManagerPlugin/RenameFile", { 
            "Filename": Filename,
            "NewFilename": NewFilename,
        })

    async def RenameFileAsync(self, Filename: str, NewFilename: str) -> Any:
        """
        Name Description Optional
        :param Filename: {str}  False
        :param NewFilename: {str}  False
        :returns: Any
        """
        return await self.api_call_async("FileManagerPlugin/RenameFile", { 
            "Filename": Filename,
            "NewFilename": NewFilename,
        })

    def TrashDirectory(self, DirectoryName: str) -> Any:
        """
        Name Description Optional
        :param DirectoryName: {str}  False
        :returns: Any
        """
        return self.api_call("FileManagerPlugin/TrashDirectory", { 
            "DirectoryName": DirectoryName,
        })

    async def TrashDirectoryAsync(self, DirectoryName: str) -> Any:
        """
        Name Description Optional
        :param DirectoryName: {str}  False
        :returns: Any
        """
        return await self.api_call_async("FileManagerPlugin/TrashDirectory", { 
            "DirectoryName": DirectoryName,
        })

    def TrashFile(self, Filename: str) -> Any:
        """
        Name Description Optional
        :param Filename: {str}  False
        :returns: Any
        """
        return self.api_call("FileManagerPlugin/TrashFile", { 
            "Filename": Filename,
        })

    async def TrashFileAsync(self, Filename: str) -> Any:
        """
        Name Description Optional
        :param Filename: {str}  False
        :returns: Any
        """
        return await self.api_call_async("FileManagerPlugin/TrashFile", { 
            "Filename": Filename,
        })

    def WriteFileChunk(self, Filename: str, Data: str, Offset: int, FinalChunk: bool) -> Any:
        """
        Name Description Optional
        :param Filename: {str}  False
        :param Data: {str}  False
        :param Offset: {int}  False
        :param FinalChunk: {bool}  False
        :returns: Any
        """
        return self.api_call("FileManagerPlugin/WriteFileChunk", { 
            "Filename": Filename,
            "Data": Data,
            "Offset": Offset,
            "FinalChunk": FinalChunk,
        })

    async def WriteFileChunkAsync(self, Filename: str, Data: str, Offset: int, FinalChunk: bool) -> Any:
        """
        Name Description Optional
        :param Filename: {str}  False
        :param Data: {str}  False
        :param Offset: {int}  False
        :param FinalChunk: {bool}  False
        :returns: Any
        """
        return await self.api_call_async("FileManagerPlugin/WriteFileChunk", { 
            "Filename": Filename,
            "Data": Data,
            "Offset": Offset,
            "FinalChunk": FinalChunk,
        })

