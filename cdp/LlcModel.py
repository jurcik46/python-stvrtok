from msilib.schema import Error
import struct

from CDPModel import CDPModel
from utils.MacUtils import MacUtils
class LlcModel:
    
    def __init__(self):
        self.dsap = 0xAA
        self.ssap = 0xAA
        self.ctrl = 0x03
        self.ouid = "00:00:0C"
        self.pid = 0x2000
        self.payload = None
    
    def add_payload(self, pa_payload:CDPModel):
        self.payload:CDPModel = pa_payload
        
    def to_bytes(self):
        if self.payload is None:
            raise Exception("Payload is empty!!!")
        
        return (struct.pack("!3B", self.dsap, self.ssap, self.ctrl)
                + MacUtils.mac_to_bytes(self.ouid)
                + struct.pack("!H", self.pid)
                + self.payload.to_bytes()
                )
        
        