from config import Config
from cv03.server.services.SocketService import SocketService

config = Config()

socket_service = SocketService(config.ip_address, config.port)
socket_service.run_server()
