import socket
import struct

from DnsHeaderyModel import DnsHeaderModel
from DnsQueryBodyModel import DnsQueryBodyModel
class DnsService:
    
    
    def generate_header(self, pa_dns_header_model:DnsHeaderModel):
        return struct.pack("!6H",
                           pa_dns_header_model.transation_id,
                           pa_dns_header_model.flags,
                           pa_dns_header_model.question_count,
                           pa_dns_header_model.answer_count,
                           pa_dns_header_model.authority_count,
                           pa_dns_header_model.additional_count
                           )
    def _fromat_domain_to_query_name(self, pa_domain):
        domain_splited = pa_domain.split(".")
        qnameb_resultb = bytes()
        for label in domain_splited:
             print(label)
             qnameb_resultb += struct.pack("!B", len(label))
             qnameb_resultb += label.encode()
        qnameb_resultb += struct.pack("!B", 0)
        return qnameb_resultb
   
    
    def generate_query_body(self, pa_dns_query_body_model:DnsQueryBodyModel):
        qnameb = self._fromat_domain_to_query_name(pa_dns_query_body_model.domain_name)
        qtypeb= struct.pack("!H", pa_dns_query_body_model.type)
        qclassb = struct.pack("!H", pa_dns_query_body_model.qclass)    
        return qnameb + qtypeb + qclassb
    
    def process_response(self, pa_response_data:bytes):
        (transaction_id, flags) = struct.unpack("!2H", pa_response_data[0:4])
        requested_ip = socket.inet_ntoa(pa_response_data[-4:])
        return (transaction_id, flags, requested_ip)
    
    
    def response_pretty(self, pa_response_data:bytes, pa_reply_addr):
         (transaction_id, flags, requested_ip ) = self.process_response(pa_response_data)
         
         print(f"Response from {pa_reply_addr[0]}:{pa_reply_addr[1]} bytes: {len(pa_response_data)}  - id: 0x{transaction_id:02X}, flags 0x{flags:02X}, address: {requested_ip}")