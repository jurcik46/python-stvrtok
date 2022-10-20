from DnsSocketService import DnsSocketService
from DnsService import DnsService
from DnsHeaderyModel import DnsHeaderModel
from DnsQueryBodyModel import DnsQueryBodyModel


dns_service = DnsService()
socket_service = DnsSocketService()

questions_text = input("Enter DNS name: ")
dns_header = DnsHeaderModel()
dns_body = DnsQueryBodyModel(questions_text)

socket_service.init_socket()


socket_service.send_data(dns_service.generate_header(dns_header) + dns_service.generate_query_body(dns_body))


