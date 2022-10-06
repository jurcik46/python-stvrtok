from config import Config
from services.SocketService import SocketService

server_config = Config()

socket_service = SocketService(server_config.ip_address, server_config.port)
socket_service.run_server()
