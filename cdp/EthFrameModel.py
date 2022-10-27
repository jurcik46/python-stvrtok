import struct

from LlcModel import LlcModel
from utils.MacUtils import MacUtils


class EthFrameModel():
    def __init__(self, pa_src_mac) -> None:
        self.dst_mac = "01:00:0C:CC:CC:CC"
        self.src_mac = pa_src_mac
        self.length = 0
        pass
    
    def add_payload(self, pa_payload:LlcModel):
        self.payload:LlcModel = pa_payload
        
    def to_bytes(self):
        payload_bytes = self.payload.to_bytes()
        self.length = len(payload_bytes)
        return (MacUtils.mac_to_bytes(self.dst_mac)
                + MacUtils.mac_to_bytes(self.src_mac)
                + struct.pack("!H",self.length)
                + payload_bytes)
        