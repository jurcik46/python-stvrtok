from TlvsModels.TlvModel import TlvModel
from TlvsModels.DeviceIdTlvModel import DeviceIdTlvModel

class SoftwareTlvModel(DeviceIdTlvModel):
    
    def __init__(self, pa_software) -> None:
        super().__init__(pa_software)
        self.type = 0x0005