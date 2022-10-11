
class ServerConfig:
    ip_address:str = ""
    port:int = 0
    def __init__(self):
        self.ip_address:str = "0.0.0.0"
        self.port:int = 9999