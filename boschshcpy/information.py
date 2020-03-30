from enum import Enum


class SHCInformation:
    class UpdateState(Enum):
        NO_UPDATE_AVAILABLE = "NO_UPDATE_AVAILABLE"
        DOWNLOADING = "DOWNLOADING"
        UPDATE_IN_PROGRESS = "UPDATE_IN_PROGRESS"
        UPDATE_AVAILABLE = "UPDATE_AVAILABLE"
        NOT_INITIALIZED = "NOT_INITIALIZED"

    def __init__(self, api, raw_information):
        self._api = api
        self._raw_information = raw_information

    @property
    def version(self):
        return self._raw_information["version"]

    @property
    def updateState(self) -> UpdateState:
        return self.UpdateState(self._raw_information["updateState"])

    @property
    def connectivityVersion(self):
        return self._raw_information["connectivityVersion"]

    def summary(self):
        print(f"Information:")
        print(f"  SW Version         : {self.version}")
        print(f"  State              : {self.updateState}")
        print(f"  connectivityVersion: {self.connectivityVersion}")