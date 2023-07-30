class Solution(object):
    def addBinary(self, a, b):
        carry = False
        dif = len(a) - len(b)
        re = ""
        if dif < 0:
            a = "0" * (-1 * dif) + a
        elif dif > 0:
            b = "0" * dif + b
        i = len(a) - 1
        while i >= 0:
            t = int(a[i]) + int(b[i]) + carry
            if t == 0 or t == 1:
                re = str(t) + re
                carry = False
            elif t == 2 or t == 3:
                re = str(t - 2) + re
                carry = True
            i -= 1
        if carry:
           re = "1" + re
        return re