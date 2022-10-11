
class ClientConfig:
    server_ip_address:str = ""
    server_port:int = 0
    user_name:str=""
    def __init__(self):
        self.server_ip_address:str = "0.0.0.0"
        self.server_port:int = 9999
        self.user_name:str = "jano"