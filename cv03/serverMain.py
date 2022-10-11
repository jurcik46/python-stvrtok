from configServer import ServerConfig
from services.SocketService import SocketService

server_config = ServerConfig()

socket_service = SocketService(server_config.ip_address, server_config.port)
socket_service.run_server()
