class Calculator:
    @staticmethod
    def add(a,b):
        return a + b

    @staticmethod
    def sub(a,b):
        return a - b

    @staticmethod
    def multi(a,b):
        return a * b

    @staticmethod
    def div(a,b):
        return a / b

    @staticmethod
    def aton(num):
        if not isinstance(num,str):
            return num
        return eval(num)


if __name__ == '__main__':
    Calculator.aton(8)