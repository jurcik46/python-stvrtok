
import struct
import socket

from DnsService import DnsService
from DnsHeaderType import DnsHeaderType
from DnsQueryBodyType import DnsQueryBodyType
from DnsSocketService import DnsSocketService

dns_service = DnsService()
socket_service = DnsSocketService()

question_text = input("Zadajte DNS meno: ")

dns_header = DnsHeaderType()
dns_body = DnsQueryBodyType(question_text)

socket_service.init_socket()


#poslanie ziadosti
socket_service.send_data(dns_service.generate_header(dns_header) + dns_service.generate_query_body(dns_body))

#prijem odpovede
reply_bytes, reply_addr = socket_service.get_response()
dns_service.response_pretty(reply_bytes, reply_addr)

socket_service.destroy_socket()

