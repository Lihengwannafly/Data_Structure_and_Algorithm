class Solution:
    def __init__(self):
        self.MININT = -2147483648
        self.MAXINT = 2147483647

    def myAtoi(self, str: str) -> int:
        flag = False
        flagn = False
        flagp = False
        flagc = False
        num = 0
        for c in str:
            if c.isspace() and not flagc:
                continue
            if c.isalpha() and not flag:
                return 0
            elif c == '-' and not flagn and not flagp and not flagc:
                flag = True
                flagn = True
                flagc = True
            elif c == '+' and not flagn and not flagp and not flagc:
                flag = True
                flagp = True
                flagc = True
            elif c.isdigit():
                flag = True
                num = num * 10 + int(c)
                flagc = True
            elif not c.isdigit():
                break
        if flagn:
            num = -num
        if num > self.MAXINT:
            return self.MAXINT
        elif num < self.MININT:
            return self.MININT
        return num