import re
class Solution:
    def myAtoi(self, str: str) -> int:
        temp = str
        try:
                num = re.match(r'^\s*(\-|\+)?[0-9]*',temp).group()
                num = int(num)
                if num>(2**31-1):
                    return 2**31-1
                if num<-2**31:
                    return -2**31
                else:
                    return num
        except:
            return 0