from TlvsModels.TlvModel import TlvModel
from utils.BitesUtils import BitesUtils
import struct

class CapabilitiesTlvModel(TlvModel):
    def __init__(self, pa_router=False, pa_switch = False, pa_host=False, pa_phone= False) -> None:
        TlvModel.__init__(self,0x0004)
        self.router = pa_router
        self.switch = pa_switch
        self.host = pa_host
        self.phone = pa_phone
        self.capabilities = 0x00000000
        
    def to_byte(self):
        self.length = 4
        
        if self.router:
            self.capabilities =  BitesUtils.set_bite(self.capabilities, 1)
        if self.switch:
            self.capabilities = BitesUtils.set_bite(self.capabilities, 4)
        if self.host:
            self.capabilities = BitesUtils.set_bite(self.capabilities, 5)
        if self.phone:
            self.capabilities = BitesUtils.set_bite(self.capabilities, 8)
        return super().to_byte() + struct.pack("!I", self.capabilities)
            
            