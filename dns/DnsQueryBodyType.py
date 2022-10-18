class DnsQueryBodyType:


    def __init__(self, pa_domain_name, pa_type = 1, pa_qclass=1  ):
        self.domain_name = pa_domain_name
        self.type = pa_type #1-A, 2-NS, 5-CNAME, 6-SOA, 15-MX
        self.qclass = pa_qclass

