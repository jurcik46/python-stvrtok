import struct
class TlvModel():
    def __init__(self, pa_type) -> None:
        self.type = pa_type
        self.length = 4
        pass
    
    
    def to_byte(self):
        return struct.pack("!2H", self.type, self.length)