from DnsHeaderyModel import DnsHeaderModel
from DnsQueryBodyModel import DnsQueryBodyModel


questions_text = input("Enter DNS name: ")
dns_header = DnsHeaderModel()
dns_body = DnsQueryBodyModel(questions_text)

