class ModulusZero:

    def divisable(self, num1, num2):
        return True if num1 % num2 == 0 else False

    def modulus(self, num1, num2):
        return num1 % num2

    def positive(self, num1, num2):
        return True if num1 >= 0 and num2 >= 0 else False
