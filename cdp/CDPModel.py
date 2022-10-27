import struct

class CDPModel():
    
    def __init__(self):
        self.version = 1
        self.ttl = 100
        self.checksum = 0x0000
        self.tlvs = list()
        
    def add_tlv(self, tlvModel):
        self.tlvs.append(tlvModel)
        
    def to_bytes(self):
        result_bytes = struct.pack("!2BH", self.version, self.ttl, self.checksum)
        for tlv in self.tlvs:
            result_bytes += tlv.to_byte()
        return result_bytes