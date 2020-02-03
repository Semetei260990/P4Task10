class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, no):
        x = complex(self.real, self.imaginary)
        y = complex(no.real, no.imaginary)
        result = x+y 
        return Complex(result.real , result.imag).__str__()
        
    def __sub__(self, no):
        x = complex(self.real, self.imaginary)
        y = complex(no.real, no.imaginary)
        result = x-y
        return Complex(result.real, result.imag).__str__()
        
    def __mul__(self, no):
        x = complex(self.real, self.imaginary)
        y = complex(no.real, no.imaginary)
        result = x*y
        return Complex(result.real, result.imag).__str__()
   
    def __truediv__(self, no):
        x = complex(self.real, self.imaginary)
        y = complex(no.real, no.imaginary)
        result = x/y
        return Complex(result.real, result.imag).__str__()
    def mod(self):
        x = complex(self.imaginary, self.real)
        result = abs(x)
        return Complex(result, 0).__str__()