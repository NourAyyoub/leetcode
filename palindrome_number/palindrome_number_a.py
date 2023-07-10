class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        digits = []
        while x > 0:
            digits.insert(0, (x % 10))
            x //= 10
        j = len(digits) - 1
        for i in range(len(digits)//2):
           if digits[i] != digits[j]:
               return False
           j -= 1
        return True
