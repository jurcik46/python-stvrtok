class DnsHeaderModel:
    
    def __init__(self, pa_transatction_id= 0x1234, pa_flags=0x0100, pa_question_count = 1, pa_answer_count = 0, pa_authority_count = 0, pa_additional_count =0 ) -> None:
        self.transation_id = pa_transatction_id
        self.flags = pa_flags
        self.question_count = pa_question_count
        self.answer_count = pa_answer_count
        self.authority_count = pa_authority_count
        self.additional_count = pa_additional_count
        pass