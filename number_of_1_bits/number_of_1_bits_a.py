class Solution(object):
    def hammingWeight(self, n):
        c = 0
        while n:
            if n % 2 == 1:
                c += 1
            n //= 2
        return c