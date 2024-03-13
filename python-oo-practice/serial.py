
"""Python serial number generator."""
class SerialGenerator:
    
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self,start = 100):#can remove start=100
        self.start = start            #initializes our current and start var
        self.current = start
    def generate(self):
        serial_num = self.current
        self.current +=1             #iterates adds one
        return serial_num
    def reset(self):
        self.current = self.start #resets back to 100
serial = SerialGenerator(start=100)

