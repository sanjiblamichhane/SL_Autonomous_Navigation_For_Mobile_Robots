
class Encoder:

    GPIONO= [2,3,4,17,22,27,10,9,11,5,6,13]
    VALID_ENC_VAL= [14,15,23,24,8,7,20,21]

    def __init__(self, pi, frequency=1000):
        self.pi = pi
        self.frequency = frequency ## set to 1k Hz

    def read_pwm(self):
        pass


    def write_pwm(self):
        '''
        - a method
        - writes pwm info
        '''
        pass









## driver
if __name__ == "__main__":
    encoder = Encoder()
