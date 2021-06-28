class ModulusZero:

    def modulus(self,num1, num2):
        return num1 % num2

    def positive(self, num1, num2):
        if num1 < 0 :
            return False
        elif num2 < 0:
            return False
        else:
            return True
