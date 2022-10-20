class DnsQueryBodyModel:
    
    def __init__(self, pa_domain_name, pa_type= 1 , pa_qclass =1 ) -> None:
        self.domain_name = pa_domain_name
        self.type = pa_type 
        self.qclass = pa_qclass
        pass