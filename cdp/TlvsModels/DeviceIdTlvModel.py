from TlvsModels.TlvModel import TlvModel


class DeviceIdTlvModel(TlvModel):
    
    def __init__(self, pa_device_id) -> None:
        TlvModel.__init__(self,0x0001)
        self.device_id = pa_device_id
    
    def to_byte(self):
        id_bytes = self.device_id.encode()
        self.length += len(id_bytes)
        return TlvModel.to_byte(self) + id_bytes
        