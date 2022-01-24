class Solution:
    def myAtoi(self, s: str) -> int:
        num = None
        symbol = None
        spaceFlag = 0
        for i in s:
            if i in ['-','+']:
                spaceFlag=1
                if symbol is not None or (num is not None):
                    if num is not None: break
                    return 0 
                else:symbol = i
            elif spaceFlag ==0 and i ==" ":
                pass
            elif (ord(i) >= ord('0') and ord(i) <=ord('9')):
                spaceFlag=1
                num = num*10 + int(i) if num is not None else int(i)
            else:
                spaceFlag=1       
                break
        if num is not None:
            if symbol=='-':
                num = max(num*-1, -2**31)
            else:
                num = min(2**31 - 1, num) 
        return num if num is not None else 0
