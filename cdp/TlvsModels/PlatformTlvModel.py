from TlvsModels.TlvModel import TlvModel
from TlvsModels.DeviceIdTlvModel import DeviceIdTlvModel

class PlatformTlvModel(DeviceIdTlvModel):
    
    def __init__(self, pa_platform) -> None:
        super().__init__(pa_platform)
        self.type = 0x0006