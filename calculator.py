class Calculator:
    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
            return a * b
        
    def divide(self, a, b):
            if b == 0:
                raise ValueError("Cannot divide by zero.")
            return a / b

    def power(self, a, b):
        return a ** b

    def sqrt(self, a):
        if a < 0:
            raise ValueError("Cannot take square root of a negative number.")
        return math.sqrt(a)
