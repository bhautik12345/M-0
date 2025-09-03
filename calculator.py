class calc:
    def __init__(self):
        print("Developer 2 update !")
        
    def sums(self, *args):
        print("sum is :",sum(args))
        
    def multi(self, *args):
        res = 1
        for ele in args:
            res = res * ele
        print("multiplication is :",res)

    def division(self, a, b):
        print("division is :",a/b)

    def subtraction(self, a, b):
        print("subtraction is :",a-b)
        
    def exponentiation(self, a, pow):
        print("expo is :",a**pow)
    
obj = calc()
obj.sums(1,2,3,4,5)
obj.multi(1,2,3)
obj.division(5,4)
obj.subtraction(5,6)
obj.exponentiation(2,5)

