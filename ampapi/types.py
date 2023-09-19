# An API that allows you to communicate with AMP installations from within Python
# Author: p0t4t0sandich

from typing import Any, Generic, NamedTuple, TypeVar
from enum import Enum

T = TypeVar('T')

class ActionResult(Generic[T]):
    """
    Generic response type for calls that return a result and a reason for failure
    Author: p0t4t0sandich
    :param Status: true if successful, false if not
    :type Status: bool
    :param Reason: Reason for failure
    :type Reason: str
    :param Result: Result of the call
    :type Result: T
    """
    Status: bool
    Reason: str
    Result: T

    def __init__(self, Status: bool, Reason: str, Result: T) -> None:
        """
        Initializes the ActionResult object
        Author: p0t4t0sandwich
        """
        self.Status = Status
        self.Reason = Reason
        self.Result = Result

class AMPVersion(NamedTuple):
    """
    AMP version information
    Author: p0t4t0sandwich
    :param Major: The major version number
    :type Major: int
    :param Minor: The minor version number
    :type Minor: int
    :param Build: The build number
    :type Build: int
    :param Revision: The revision number
    :type Revision: int
    :param MajorRevision: The major revision number
    :type MajorRevision: int
    :param MinorRevision: The minor revision number
    :type MinorRevision: int
    """
    Major: int
    Minor: int
    Build: int
    Revision: int
    MajorRevision: int
    MinorRevision: int

# Type alias for AMPVersion
# Author: p0t4t0sandwich
AMPVersionAlias = AMPVersion

class Branding(NamedTuple):
    """
    Branding information
    Author: p0t4t0sandwich
    :param DisplayBranding: Whether to display branding
    :type DisplayBranding: bool
    :param PageTitle: The page title
    :type PageTitle: str
    :param CompanyName: The company name
    :type CompanyName: str
    :param WelcomeMessage: The welcome message
    :type WelcomeMessage: str
    :param BrandingMessage: The branding message
    :type BrandingMessage: str
    :param ShortBrandingMessage: The short branding message
    :type ShortBrandingMessage: str
    :param URL: The URL
    :type URL: str
    :param SupportURL: The support URL
    :type SupportURL: str
    :param SupportText: The support text
    :type SupportText: str
    :param SubmitTicketURL: The submit ticket URL
    :type SubmitTicketURL: str
    :param LogoURL: The logo URL
    :type LogoURL: str
    :param BackgroundURL: The background URL
    :type BackgroundURL: str
    :param SplashFrameURL: The splash frame URL
    :type SplashFrameURL: str
    :param ForgotPasswordURL: The forgot password URL
    :type ForgotPasswordURL: str
    """
    DisplayBranding: bool
    PageTitle: str
    CompanyName: str
    WelcomeMessage: str
    BrandingMessage: str
    ShortBrandingMessage: str
    URL: str
    SupportURL: str
    SupportText: str
    SubmitTicketURL: str
    LogoURL: str
    BackgroundURL: str
    SplashFrameURL: str
    ForgotPasswordURL: str

class ConsoleEntry(NamedTuple):
    """
    Struct for the result of API.Core#GetUpdates.ConsoleEntries
    Author: p0t4t0sandwich
    :param Timestamp: The timestamp of the console entry
    :type Timestamp: str
    :param Source: The source of the console entry
    :type Source: str
    :param SourceId: The source ID of the console entry
    :type SourceId: str
    :param Type: The type of the console entry
    :type Type: str
    :param Contents: The contents of the console entry
    :type Contents: str
    """
    Timestamp: str
    Source: str
    SourceId: str
    Type: str
    Contents: str

class CPUInfo(NamedTuple):
    """
    CPU information object
    Author: p0t4t0sandwich
    :param Sockets: Number of CPU sockets
    :type Sockets: int
    :param Cores: Number of CPU cores
    :type Cores: int
    :param Threads: Number of CPU threads
    :type Threads: int
    :param Vendor: CPU vendor
    :type Vendor: str
    :param ModelName: CPU model name
    :type ModelName: str
    :param TotalCores: Total number of CPU cores
    :type TotalCores: int
    :param TotalThreads: Total number of CPU threads
    :type TotalThreads: int
    """
    Sockets: int
    Cores: int
    Threads: int
    Vendor: str
    ModelName: str
    TotalCores: int
    TotalThreads: int

# Type alias for CPUInfo
# Author: p0t4t0sandwich
CPUInfoAlias = CPUInfo

class EndpointInfo(NamedTuple):
    """
    An application endpoint object
    Author: p0t4t0sandwich
    :param DisplayName: The display name of the endpoint
    :type DisplayName: str
    :param Endpoint: The endpoint address
    :type Endpoint: str
    :param Uri: The URI of the endpoint
    :type Uri: str
    """
    DisplayName: str
    Endpoint: str
    Uri: str

# A UUID is a string that represents a UUID
# Author: p0t4t0sandwich
UUID = str

class InstanceDatastore(NamedTuple):
    """
    A datastore object
    Author: p0t4t0sandwich
    :param Id: The datastore ID
    :type Id: int
    :param FriendlyName: The friendly name
    :type FriendlyName: str
    """
    Id: int
    FriendlyName: str

class State(Enum):
    """
    Represents the state of an instance
    Author: p0t4t0sandwich
    """
    Undefined = -1
    Stopped = 0
    PreStart = 5
    Configuring = 7 # The server is performing some first-time-start configuration.
    Starting = 10
    Ready = 20
    Restarting = 30 # Server is in the middle of stopping, but once shutdown has finished it will automatically restart.
    Stopping = 40
    PreparingForSleep = 45
    Sleeping = 50 # The application should be able to be resumed quickly if using this state. Otherwise use Stopped.
    Waiting = 60 # The application is waiting for some external service/application to respond/become available.
    Installing = 70
    Updating = 75
    AwaitingUserInput = 80 # Used during installation, means that some user input is required to complete setup (authentication etc).
    Failed = 100
    Suspended = 200
    Maintainence = 250
    Indeterminate = 999 # The state is unknown, or doesn't apply (for modules that don't start an external process)

# Type alias for State
# Author: p0t4t0sandwich
StateAlias = State

def StateMapReverse(state: State) -> str:
    """
    A map of integer values to their states
    Author: p0t4t0sandwich
    :param state: The state
    :type state: State
    :return: The state name
    :rtype: str
    """
    return state.name

class Metric():
    """
    A metric object
    Author: p0t4t0sandwich
    :param RawValue: The raw value
    :type RawValue: int
    :param MaxValue: The maximum value
    :type MaxValue: int
    :param Percent: The percentage
    :type Percent: float
    :param Units: The units
    :type Units: str
    :param Color: The color
    :type Color: str
    :param Color2: The second color
    :type Color2: str
    :param Color3: The third color
    :type Color3: str
    """
    RawValue: int
    MaxValue: int
    Percent: float
    Units: str
    Color: str
    Color2: str
    Color3: str

    def __init__(self, RawValue: int, MaxValue: int, Percent: float, Units: str, Color: str = "", Color2: str = "", Color3: str = "") -> None:
        """
        Initializes the Metric object
        Author: p0t4t0sandwich
        """
        self.RawValue = RawValue
        self.MaxValue = MaxValue
        self.Percent = Percent
        self.Units = Units
        self.Color = Color
        self.Color2 = Color2
        self.Color3 = Color3

class Instance():
    """
    An instance object
    Author: p0t4t0sandwich
    :param InstanceID: The instance ID
    :type InstanceID: UUID
    :param TargetID: The target ID
    :type TargetID: UUID
    :param InstanceName: The instance name
    :type InstanceName: str
    :param FriendlyName: The friendly name
    :type FriendlyName: str
    :param Description: The description
    :type Description: str
    :param Module: The module
    :type Module: str
    :param ModuleDisplayName: The module display name
    :type ModuleDisplayName: str
    :param AMPVersion: The AMP version
    :type AMPVersion: AMPVersion
    :param IsHTTPS: Whether HTTPS is enabled
    :type IsHTTPS: bool
    :param IP: The IP address
    :type IP: str
    :param Port: The port
    :type Port: int
    :param Daemon: Whether the instance is a daemon
    :type Daemon: bool
    :param DaemonAutostart: Whether the instance daemon autostarts
    :type DaemonAutostart: bool
    :param ExcludeFromFirewall: Whether the instance is excluded from the firewall
    :type ExcludeFromFirewall: bool
    :param Running: Whether the instance is running
    :type Running: bool
    :param AppState: The application state
    :type AppState: State
    :param Tags: The tags
    :type Tags: list[str]
    :param DiskUsageMB: The disk usage in MB
    :type DiskUsageMB: int
    :param ReleaseStream: The release stream
    :type ReleaseStream: str
    :param ManagementMode: The management mode
    :type ManagementMode: str
    :param Suspended: Whether the instance is suspended
    :type Suspended: bool
    :param IsContainerInstance: Whether the instance is a container instance
    :type IsContainerInstance: bool
    :param ContainerMemoryMB: The container memory in MB
    :type ContainerMemoryMB: int
    :param ContainerMemoryPolicy: The container memory policy
    :type ContainerMemoryPolicy: str
    :param ContainerCPUs: The container CPUs
    :type ContainerCPUs: int
    :param SpecificDockerImage: The specific Docker image
    :type SpecificDockerImage: str
    :param Metrics: The metrics
    :type Metrics: dict[str, Metric]
    :param ApplicationEndpoints: The application endpoints
    :type ApplicationEndpoints: list[EndpointInfo]
    :param DeploymentArgs: The deployment arguments
    :type DeploymentArgs: dict[str, str]
    :param DisplayImageSource: The display image source
    :type DisplayImageSource: str
    """
    InstanceID: UUID
    TargetID: UUID
    InstanceName: str
    FriendlyName: str
    Description: str
    Module: str
    ModuleDisplayName: str
    AMPVersion: AMPVersionAlias
    IsHTTPS: bool
    IP: str
    Port: int
    Daemon: bool
    DaemonAutostart: bool
    ExcludeFromFirewall: bool
    Running: bool
    AppState: State
    Tags: list[str]
    DiskUsageMB: int
    ReleaseStream: str
    ManagementMode: str
    Suspended: bool
    IsContainerInstance: bool
    ContainerMemoryMB: int
    ContainerMemoryPolicy: str
    ContainerCPUs: int
    SpecificDockerImage: str
    Metrics: dict[str, Metric]
    ApplicationEndpoints: list[EndpointInfo]
    DeploymentArgs: dict[str, str]
    DisplayImageSource: str

    def __init__(self, InstanceID: UUID, TargetID: UUID, InstanceName: str, FriendlyName: str, Module: str, AMPVersion: AMPVersionAlias, IsHTTPS: bool, IP: str, Port: int, Daemon: bool, DaemonAutostart: bool, ExcludeFromFirewall: bool, Running: bool, AppState: State, Tags: list[str], DiskUsageMB: int, ReleaseStream: str, ManagementMode: str, Suspended: bool, IsContainerInstance: bool, ContainerMemoryMB: int, ContainerMemoryPolicy: str, ContainerCPUs: int, Metrics: dict[str, Metric], ApplicationEndpoints: list[EndpointInfo], DeploymentArgs: dict[str, str], DisplayImageSource: str = "", Description: str = "", ModuleDisplayName: str = "", SpecificDockerImage: str = "") -> None:
        """
        Initializes the Instance object
        Author: p0t4t0sandwich
        """
        self.InstanceID = InstanceID
        self.TargetID = TargetID
        self.InstanceName = InstanceName
        self.FriendlyName = FriendlyName
        self.Description = Description
        self.Module = Module
        self.ModuleDisplayName = ModuleDisplayName
        self.AMPVersion = AMPVersion
        self.IsHTTPS = IsHTTPS
        self.IP = IP
        self.Port = Port
        self.Daemon = Daemon
        self.DaemonAutostart = DaemonAutostart
        self.ExcludeFromFirewall = ExcludeFromFirewall
        self.Running = Running
        self.AppState = AppState
        self.Tags = Tags
        self.DiskUsageMB = DiskUsageMB
        self.ReleaseStream = ReleaseStream
        self.ManagementMode = ManagementMode
        self.Suspended = Suspended
        self.IsContainerInstance = IsContainerInstance
        self.ContainerMemoryMB = ContainerMemoryMB
        self.ContainerMemoryPolicy = ContainerMemoryPolicy
        self.ContainerCPUs = ContainerCPUs
        self.Metrics = {i : Metric(**Metrics[i]) for i in Metrics}
        self.ApplicationEndpoints = [EndpointInfo(**ApplicationEndpoints[i]) for i in range(len(ApplicationEndpoints))]
        self.DeploymentArgs = DeploymentArgs
        self.DisplayImageSource = DisplayImageSource

class PlatformInfo():
    """
    Platform information object
    Author: p0t4t0sandwich
    :param CPUInfo: The CPU information object
    :type CPUInfo: CPUInfo
    :param InstalledRAMMB: The installed RAM in MB
    :type InstalledRAMMB: int
    :param OS: The OS
    :type OS: int
    :param PlatformName: The platform name
    :type PlatformName: str
    :param SystemType: The system type
    :type SystemType: int
    :param Virtualization: The virtualization
    :type Virtualization: int
    """
    CPUInfo: CPUInfoAlias
    InstalledRAMMB: int
    OS: int
    PlatformName: str
    SystemType: int
    Virtualization: int

    def __init__(self, CPUInfo: CPUInfoAlias, InstalledRAMMB: int, OS: int, PlatformName: str, SystemType: int, Virtualization: int) -> None:
        """
        Initializes the PlatformInfo object
        Author: p0t4t0sandwich
        """
        self.CPUInfo = CPUInfoAlias(**CPUInfo)
        self.InstalledRAMMB = InstalledRAMMB
        self.OS = OS
        self.PlatformName = PlatformName
        self.SystemType = SystemType
        self.Virtualization = Virtualization

# Type alias for PlatformInfo
# Author: p0t4t0sandwich
PlatformInfoAlias = PlatformInfo

class IADSInstance():
    """
    An ADS instance object
    Author: p0t4t0sandwich
    :param Id: The ADS instance ID
    :type Id: int
    :param InstanceId: The instance ID
    :type InstanceId: UUID
    :param FriendlyName: The friendly name
    :type FriendlyName: str
    :param Description: The description
    :type Description: str
    :param Disabled: Whether the instance is disabled
    :type Disabled: bool
    :param IsRemote: Whether the instance is remote
    :type IsRemote: bool
    :param Platform: The platform information object
    :type PlatformInfo: Platform
    :param Datastores: The datastores
    :type Datastores: list[InstanceDatastore]
    :param CreatesInContainers: Whether the instance creates in containers
    :type CreatesInContainers: bool
    :param State: The state
    :type State: State
    :param StateReason: The state reason
    :type StateReason: str
    :param CanCreate: Whether the instance can create
    :type CanCreate: bool
    :param LastUpdated: The last updated
    :type LastUpdated: str
    :param AvailableInstances: The available instances
    :type AvailableInstances: list[Instance]
    :param AvailableIPs: The available IPs
    :type AvailableIPs: list[str]
    """
    Id: int
    InstanceId: UUID
    FriendlyName: str
    Description: str
    Disabled: bool
    IsRemote: bool
    Platform: PlatformInfo
    Datastores: list[InstanceDatastore]
    CreatesInContainers: bool
    State: State
    StateReason: str
    CanCreate: bool
    LastUpdated: str
    AvailableInstances: list[Instance]
    AvailableIPs: list[str]
    Tags: list[str]
    TagsList: list[str]
    URL: str

    def __init__(self, Id: int, InstanceId: UUID, FriendlyName: str, Disabled: bool, IsRemote: bool, Platform: PlatformInfo, Datastores: list[InstanceDatastore], CreatesInContainers: bool, State: StateAlias, StateReason: str, CanCreate: bool, LastUpdated: str, AvailableInstances: list[Instance], AvailableIPs: list[str], Description: str = "", Tags: list[str] = [], TagsList: list[str] = [], URL: str = "") -> None:
        """
        Initializes the IADSInstance object
        Author: p0t4t0sandwich
        """
        self.Id = Id
        self.InstanceId = InstanceId
        self.FriendlyName = FriendlyName
        self.Description = Description
        self.Disabled = Disabled
        self.IsRemote = IsRemote
        self.Platform = PlatformInfo(**Platform)
        self.Datastores = [InstanceDatastore(**Datastores[i]) for i in range(len(Datastores))]
        self.CreatesInContainers = CreatesInContainers
        self.State = State
        self.StateReason = StateReason
        self.CanCreate = CanCreate
        self.LastUpdated = LastUpdated

        # for i in AvailableInstances:
        #     print(i.keys())

        self.AvailableInstances = [Instance(**AvailableInstances[i]) for i in range(len(AvailableInstances))]
        self.AvailableIPs = AvailableIPs
        self.URL = URL

class UserInfo(NamedTuple):
    """
    Information about the user
    Author: p0t4t0sandwich
    :param ID: The user ID
    :type ID: UUID
    :param Username: The username
    :type Username: str
    :param EmailAddress: The email address
    :type EmailAddress: str
    :param IsTwoFactorEnabled: Whether 2FA is enabled
    :type IsTwoFactorEnabled: bool
    :param Disabled: Whether the user is disabled
    :type Disabled: bool
    :param LastLogin: The last login
    :type LastLogin: str
    :param GravatarHash: The Gravatar hash
    :type GravatarHash: str
    :param IsLDAPUser: Whether the user is an LDAP user
    :type IsLDAPUser: bool
    """
    ID: UUID
    Username: str
    EmailAddress: str
    IsTwoFactorEnabled: bool
    Disabled: bool
    LastLogin: str
    GravatarHash: str
    IsLDAPUser: bool

class LoginResult():
    """
    Response type for API.Core.Login
    Author: p0t4t0sandwich
    :param success: Whether the login was successful
    :type success: bool
    :param permissions: The user's permissions
    :type permissions: list[str]
    :param sessionID: The session ID
    :type sessionID: str
    :param rememberMeToken: The remember me token
    :type rememberMeToken: str
    :param userInfo: The user information
    :type userInfo: UserInfo
    :param result: The result
    :type result: float
    """
    success: bool
    permissions: list[str]
    sessionID: str
    rememberMeToken: str
    userInfo: UserInfo
    result: float

    def __init__(self, success: bool, permissions: list[str], sessionID: str, rememberMeToken: str, userInfo: UserInfo, result: float) -> None:
        """
        Initializes the LoginResult object
        Author: p0t4t0sandwich
        """
        self.success = success
        self.permissions = permissions
        self.sessionID = sessionID
        self.rememberMeToken = rememberMeToken
        self.userInfo = UserInfo(**userInfo)
        self.result = result

class Message(NamedTuple):
    """
    Message type for API.Core.GetUpdates status messages (along with WS keep alive)
    Author: p0t4t0sandwich
    :param Id: The message ID
    :type Id: UUID
    :param Expired: Whether the message has expired
    :type Expired: bool
    :param Source: The source of the message
    :type Source: str
    :param Message: The message
    :type Message: str
    :param AgeMinutes: The age of the message in minutes
    :type AgeMinutes: int
    """
    Id: UUID
    Expired: bool
    Source: str
    Message: str
    AgeMinutes: int

class ModuleInfo(NamedTuple):
    """
    A struct to represent the object returned by the ADSModule#GetModuleInfo() method
    Author: p0t4t0sandwich
    :param Name: The name of the module
    :type Name: str
    :param Author: The author of the module
    :type Author: str
    :param AppName: The application name
    :type AppName: str
    :param SupportsSleep: Whether the module supports sleep mode
    :type SupportsSleep: bool
    :param LoadedPlugins: The loaded plugins
    :type LoadedPlugins: list[str]
    :param AMPVersion: The AMP version
    :type AMPVersion: AMPVersion
    :param AMPBuild: The AMP build
    :type AMPBuild: str
    :param ToolsVersion: The tools version
    :type ToolsVersion: AMPVersion
    :param APIVersion: The API version
    :type APIVersion: AMPVersion
    :param VersionCodename: The version codename
    :type VersionCodename: str
    :param Timestamp: The timestamp
    :type Timestamp: str
    :param BuildSpec: The build spec
    :type BuildSpec: str
    :param Branding: The branding object
    :type Branding: Branding
    :param Analytics: Whether analytics are enabled
    :type Analytics: bool
    :param FeatureSet: The feature set
    :type FeatureSet: list[str]
    :param InstanceId: The instance ID
    :type InstanceId: UUID
    :param InstanceName: The instance name
    :type InstanceName: str
    :param FriendlyName: The friendly name
    :type FriendlyName: str
    :param EndpointURI: The endpoint URI
    :type EndpointURI: str
    :param PrimaryEndpoint: The primary endpoint
    :type PrimaryEndpoint: str
    :param ModuleName: The module name
    :type ModuleName: str
    :param IsRemoteInstance: Whether the instance is remote
    :type IsRemoteInstance: bool
    :param DisplayBaseURI: The display base URI
    :type DisplayBaseURI: str
    :param RequiresFullLoad: Whether the module requires a full load
    :type RequiresFullLoad: bool
    :param AllowRememberMe: Whether remember me is allowed
    :type AllowRememberMe: bool
    """
    Name: str
    Author: str
    AppName: str
    SupportsSleep: bool
    LoadedPlugins: list[str]
    AMPVersion: AMPVersionAlias
    AMPBuild: str
    ToolsVersion: AMPVersionAlias
    APIVersion: AMPVersionAlias
    VersionCodename: str
    Timestamp: str
    BuildSpec: str
    Branding: Branding
    Analytics: bool
    FeatureSet: list[str]
    InstanceId: UUID
    InstanceName: str
    FriendlyName: str
    EndpointURI: str
    PrimaryEndpoint: str
    ModuleName: str
    IsRemoteInstance: bool
    DisplayBaseURI: str
    RequiresFullLoad: bool
    AllowRememberMe: bool

class RemoteTargetInfo():
    """
    A struct to represent the object returned by the ADSModule#GetTargetInfo() method
    Author: p0t4t0sandwich
    :param IPAddressList: The IP address list
    :type IPAddressList: list[str]
    :param PlatformInfo: The platform information object
    :type PlatformInfo: PlatformInfo
    :param Datastores: The datastores
    :type Datastores: list[InstanceDatastore]
    :param DeploysInContainers: Whether the target deploys in containers
    :type DeploysInContainers: bool
    """
    IPAddressList: list[str]
    PlatformInfo: PlatformInfoAlias
    Datastores: list[InstanceDatastore]
    DeploysInContainers: bool

    def __init__(self, IPAddressList: list[str], PlatformInfo: PlatformInfoAlias, Datastores: list[InstanceDatastore], DeploysInContainers: bool) -> None:
        """
        Initializes the RemoteTargetInfo object
        Author: p0t4t0sandwich
        """
        self.IPAddressList = IPAddressList
        self.PlatformInfo = PlatformInfoAlias(**PlatformInfo)
        self.Datastores = [InstanceDatastore(**Datastores[i]) for i in range(len(Datastores))]
        self.DeploysInContainers = DeploysInContainers

class Result(Generic[T]):
    """
    Generic response type for calls that return a result
    Author: p0t4t0sandwich
    :param result: The result object
    :type result: T
    """
    result: T

    def __init__(self, result: T) -> None:
        """
        Initializes the Result object
        Author: p0t4t0sandwich
        """

        # TODO: Replace this with a more elegant solution

        if type(result) == list:
            if len(result) == 0:
                self.result = []
                return

            keys = result[0].keys()
            if "DisplayName" in keys and "Endpoint" in keys and "Uri" in keys:
                self.result = [EndpointInfo(**result[i]) for i in range(len(result))]
            elif "Id" in keys and "InstanceId" in keys and "FriendlyName" in keys and "Disabled" in keys and "IsRemote" in keys and "Platform" in keys and "Datastores" in keys and "CreatesInContainers" in keys and "State" in keys and "StateReason" in keys and "CanCreate" in keys and "LastUpdated" in keys and "AvailableInstances" in keys and "AvailableIPs" in keys:
                self.result = [IADSInstance(**result[i]) for i in range(len(result))]
            elif "IsPrimaryTask" in keys and "StartTime" in keys and "Id" in keys and "Name" in keys and "Description" in keys and "HideFromUI" in keys and "FastDismiss" in keys and "LastUpdatePushed" in keys and "ProgressPercent" in keys and "IsCancellable" in keys and "Origin" in keys and "IsIndeterminate" in keys and "State" in keys and "Status" in keys:
                self.result = [RunningTask(**result[i]) for i in range(len(result))]
            else:
                self.result = result

        elif type(result) == dict:
            keys = result.keys()
            if "IsPrimaryTask" in keys and "StartTime" in keys and "Id" in keys and "Name" in keys and "Description" in keys and "HideFromUI" in keys and "FastDismiss" in keys and "LastUpdatePushed" in keys and "ProgressPercent" in keys and "IsCancellable" in keys and "Origin" in keys and "IsIndeterminate" in keys and "State" in keys and "Status" in keys:
                self.result = RunningTask(**result)
            elif "Id" in keys and "InstanceId" in keys and "FriendlyName" in keys and "Disabled" in keys and "IsRemote" in keys and "Platform" in keys and "Datastores" in keys and "CreatesInContainers" in keys and "State" in keys and "StateReason" in keys and "CanCreate" in keys and "LastUpdated" in keys and "AvailableInstances" in keys and "AvailableIPs" in keys:
                self.result = IADSInstance(**result)
            elif "Name" in keys and "Author" in keys and "AppName" in keys and "SupportsSleep" in keys and "LoadedPlugins" in keys and "AMPVersion" in keys and "AMPBuild" in keys and "ToolsVersion" in keys and "APIVersion" in keys and "VersionCodename" in keys and "Timestamp" in keys and "BuildSpec" in keys and "Branding" in keys and "Analytics" in keys and "FeatureSet" in keys and "InstanceId" in keys and "InstanceName" in keys and "FriendlyName" in keys and "EndpointURI" in keys and "PrimaryEndpoint" in keys and "ModuleName" in keys and "IsRemoteInstance" in keys and "DisplayBaseURI" in keys and "RequiresFullLoad" in keys and "AllowRememberMe" in keys:
                self.result = ModuleInfo(**result)
            elif "UpdateAvailable" in keys and "Version" in keys and "Build" in keys and "ReleaseNotesURL" in keys and "ToolsVersion" in keys and "PatchOnly" in keys:
                self.result = UpdateInfo(**result)
            else:
                self.result = result
        else:
            self.result = result

class RunningTask(NamedTuple):
    """
    A running task object returned by the Core#GetTasks() method
    Author: p0t4t0sandwich
    :param IsPrimaryTask: Whether the task is the primary task
    :type IsPrimaryTask: bool
    :param StartTime: The start time
    :type StartTime: str
    :param Id: The task ID
    :type Id: UUID
    :param Name: The task name
    :type Name: str
    :param Description: The task description
    :type Description: str
    :param HideFromUI: Whether the task is hidden from the UI
    :type HideFromUI: bool
    :param FastDismiss: Whether the task can be dismissed quickly
    :type FastDismiss: bool
    :param LastUpdatePushed: The last update pushed
    :type LastUpdatePushed: str
    :param ProgressPercent: The progress percentage
    :type ProgressPercent: float
    :param IsCancellable: Whether the task is cancellable
    :type IsCancellable: bool
    :param Origin: The origin
    :type Origin: str
    :param IsIndeterminate: Whether the task is indeterminate
    :type IsIndeterminate: bool
    :param State: The state
    :type State: int
    :param Status: The status
    :type Status: str
    """
    IsPrimaryTask: bool
    StartTime: str
    Id: UUID
    Name: str
    Description: str
    HideFromUI: bool
    FastDismiss: bool
    LastUpdatePushed: str
    ProgressPercent: float
    IsCancellable: bool
    Origin: str
    IsIndeterminate: bool
    State: int
    Status: str

class Spec(NamedTuple):
    """
    A setting specification object
    Author: p0t4t0sandwich
    :param ReadOnly: Whether the setting is read-only
    :type ReadOnly: bool
    :param Name: The name
    :type Name: str
    :param Description: The description
    :type Description: str
    :param Category: The category
    :type Category: str
    :param CurrentValue: The current value
    :type CurrentValue: Any
    :param ValType: The value type
    :type ValType: str
    :param EnumValues: The enum values
    :type EnumValues: Any
    :param EnumValuesAreDeferred: Whether the enum values are deferred
    :type EnumValuesAreDeferred: bool
    :param Node: The node
    :type Node: str
    :param InputType: The input type
    :type InputType: str
    :param SelectionSource: The selection source
    :type SelectionSource: Any
    :param IsProvisionSpec: Whether the setting is a provision spec
    :type IsProvisionSpec: bool
    :param ReadOnlyProvision: Whether the provision is read-only
    :type ReadOnlyProvision: bool
    :param Actions: The actions
    :type Actions: list[Any]
    :param Keywords: The keywords
    :type Keywords: Any
    :param AlwaysAllowRead: Whether the setting is always allowed to be read
    :type AlwaysAllowRead: bool
    :param Tag: The tag
    :type Tag: str
    :param MaxLength: The max length
    :type MaxLength: int
    :param Placeholder: The placeholder
    :type Placeholder: str
    :param Suffix: The suffix
    :type Suffix: str
    :param Meta: The meta
    :type Meta: str
    :param RequiresRestart: Whether the setting requires a restart
    :type RequiresRestart: bool
    """
    ReadOnly: bool
    Name: str
    Description: str
    Category: str
    CurrentValue: Any
    ValType: str
    EnumValues: Any
    EnumValuesAreDeferred: bool
    Node: str
    InputType: str
    SelectionSource: Any
    IsProvisionSpec: bool
    ReadOnlyProvision: bool
    Actions: list[Any]
    Keywords: Any
    AlwaysAllowRead: bool
    Tag: str
    MaxLength: int
    Placeholder: str
    Suffix: str
    Meta: str
    RequiresRestart: bool

class SettingsSpec():
    """
    Response object for Core.GetSettingsSpec()
    Author: p0t4t0sandwich
    :param result: The result
    :type result: dict[str, Spec]
    """
    result: dict[str, Spec]

    def __init__(self, result: dict[str, Spec]) -> None:
        """
        Initializes the SettingsSpec object
        Author: p0t4t0sandwich
        """
        self.result = {i : Spec(**result[i]) for i in result}

class Status():
    """
    Struct for the result of API.Core.GetStatus
    Author: p0t4t0sandwich
    :param State: The state of the instance
    :type State: State
    :param Uptime: The uptime of the instance
    :type Uptime: str
    :param Metrics: The metrics
    :type Metrics: dict[str, Metric]
    """
    State: StateAlias
    Uptime: str
    Metrics: dict[str, Metric]

    def __init__(self, State: StateAlias, Uptime: str, Metrics: dict[str, Metric]) -> None:
        """
        Initializes the Status struct
        Author: p0t4t0sandwich
        """
        self.State = State
        self.Uptime = Uptime
        self.Metrics = {i : Metric(**Metrics[i]) for i in Metrics}

class Task(Generic[T]):
    """
    Generic response type for calls that return a result
    Author: p0t4t0sandwich
    :param result: The result object
    :type result: T
    """
    result: T

    def __init__(self, result: T) -> None:
        """
        Initializes the Task object
        Author: p0t4t0sandwich
        """
        if type(result) == list:
            if len(result) == 0:
                self.result = []
                return

            keys = result[0].keys()
            if "ID" in keys and "Username" in keys and "EmailAddress" in keys and "IsTwoFactorEnabled" in keys and "Disabled" in keys and "LastLogin" in keys and "GravatarHash" in keys and "IsLDAPUser" in keys:
                self.result = [UserInfo(**result[i]) for i in range(len(result))]
            else:
                self.result = result

        elif type(result) == dict:
            keys = result.keys()
            if "IsPrimaryTask" in keys and "StartTime" in keys and "Id" in keys and "Name" in keys and "Description" in keys and "HideFromUI" in keys and "FastDismiss" in keys and "LastUpdatePushed" in keys and "ProgressPercent" in keys and "IsCancellable" in keys and "Origin" in keys and "IsIndeterminate" in keys and "State" in keys and "Status" in keys:
                self.result = RunningTask(**result)
            elif "ID" in keys and "Username" in keys and "EmailAddress" in keys and "IsTwoFactorEnabled" in keys and "Disabled" in keys and "LastLogin" in keys and "GravatarHash" in keys and "IsLDAPUser" in keys:
                self.result = UserInfo(**result)
            else:
                self.result = result
        else:
            self.result = result

class UpdateInfo(NamedTuple):
    """
    A struct to represent the object returned by the ADSModule#GetUpdateInfo() method
    Author: p0t4t0sandwich
    :param UpdateAvailable: Whether an update is available
    :type UpdateAvailable: bool
    :param Version: The version of the update
    :type Version: str
    :param Build: The build of the update
    :type Build: str
    :param ReleaseNotesURL: The URL to the release notes
    :type ReleaseNotesURL: str
    :param ToolsVersion: The version of the tools
    :type ToolsVersion: str
    :param PatchOnly: Whether the update is a patch
    :type PatchOnly: bool
    """
    UpdateAvailable: bool
    Version: str
    Build: str
    ReleaseNotesURL: str
    ToolsVersion: str
    PatchOnly: bool

class Updates():
    """
    Response type for API.Core.GetUpdates
    Author: p0t4t0sandwich
    :param Status: The status of the server
    :type Status: Status
    :param ConsoleEntries: The console entries of the server
    :type ConsoleEntries: list[ConsoleEntry]
    :param Messages: The messages of the server
    :type Messages: list[Message]
    :param Tasks: The tasks of the server
    :type Tasks: list[str]
    :param Ports: The ports of the server
    :type Ports: list[str]
    """
    Status: Status
    ConsoleEntries: list[ConsoleEntry]
    Messages: list[Message]
    Tasks: list[str]
    Ports: list[str]

    def __init__(self, Status: Status, ConsoleEntries: list[ConsoleEntry], Messages: list[Message], Tasks: list[str], Ports: list[str]) -> None:
        """
        Initializes the Updates object
        Author: p0t4t0sandwich
        """
        self.Status = Status
        self.ConsoleEntries = [ConsoleEntry(**ConsoleEntries[i]) for i in range(len(ConsoleEntries))]
        self.Messages = [Message(**Messages[i]) for i in range(len(Messages))]
        self.Tasks = Tasks
        self.Ports = Ports

# A URL is a string that represents a URL
# Author: p0t4t0sandwich
URL = str

class Void():
    """
    Workaround for the lack of a void type in Python
    Author: p0t4t0sandwich
    """
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """
        Initializes the Void object
        Author: p0t4t0sandwich
        """
        pass