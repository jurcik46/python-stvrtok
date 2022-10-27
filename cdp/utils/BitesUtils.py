
class BitesUtils():
    
    @staticmethod
    def set_bite(pa_input, pa_bit):
        return pa_input | (1<<(pa_bit-1))