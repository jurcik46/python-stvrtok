
class MacUtils():
    
    @staticmethod
    def mac_to_bytes(pa_mac_address):
        return bytes.fromhex(pa_mac_address.replace(":",""))
        