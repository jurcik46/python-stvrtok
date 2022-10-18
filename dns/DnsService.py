import struct
import socket


from DnsHeaderType import DnsHeaderType
from DnsQueryBodyType import DnsQueryBodyType


class DnsService:
    def generate_header(self, pa_dns_header:DnsHeaderType = 1):
        return struct.pack("!6H",
                           pa_dns_header.transaction_id,
                           pa_dns_header.flags,
                           pa_dns_header.question_count,
                           pa_dns_header.answer_count,
                           pa_dns_header.authority_count,
                           pa_dns_header.additional_count)

    def _format_domain_to_query_name(self, pa_domain):
        question_list = pa_domain.split(".")
        print(question_list)
        qname = bytes()
        for label in question_list:
            print(label)
            print(len(label))
            qname += struct.pack("!B", len(label))
            qname += label.encode()
        print(qname.decode())
        qname += struct.pack("!B", 0)
        return qname

    def generate_query_body(self, pa_dns_query_body:DnsQueryBodyType):
        qnameb = self._format_domain_to_query_name(pa_dns_query_body.domain_name)
        qtypeb = struct.pack("!H", pa_dns_query_body.type)
        qclassb = struct.pack("!H", pa_dns_query_body.qclass)
        return qnameb + qtypeb + qclassb

    def process_response(self, pa_response_data_bytes):
        (transaction_id, flags) = struct.unpack("!2H", pa_response_data_bytes[0:4])
        requested_ip = socket.inet_ntoa(pa_response_data_bytes[-4:])
        #TODO respon model
        return transaction_id, flags, requested_ip

    def response_pretty(self, pa_response_data_bytes, pa_reply_addr ):
        (transaction_id, flags, ip) = self.process_response(pa_response_data_bytes)

        print(f"Odpoved od {pa_reply_addr[0]}:{pa_reply_addr[1]} bytes: {len(pa_response_data_bytes)} - id: 0x{transaction_id:02X}, flags: 0x{flags:02X}, addr: {ip}")


