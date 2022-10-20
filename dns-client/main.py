from DnsSocketService import DnsSocketService
from DnsService import DnsService
from DnsHeaderyModel import DnsHeaderModel
from DnsQueryBodyModel import DnsQueryBodyModel


dns_service = DnsService()
socket_service = DnsSocketService("158.193.152.4")

questions_text = input("Enter DNS name: ")
dns_header = DnsHeaderModel()
dns_body = DnsQueryBodyModel(questions_text)

socket_service.init_socket()


socket_service.send_data(dns_service.generate_header(dns_header) + dns_service.generate_query_body(dns_body))

reply_bytes, reply_addr = socket_service.get_response()

dns_service.response_pretty(reply_bytes, reply_addr)


socket_service.destroy_socket()