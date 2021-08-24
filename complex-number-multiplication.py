class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        def convNum(num):
            r,i = num.split("+")
            return int(r),int(i[0:len(i)-1])
        
        a,b = convNum(num1)
        c,d = convNum(num2)
        
        return str(a*c - b*d)+"+"+str(a*d + b*c)+"i"
