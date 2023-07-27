class Solution(object):
    def plusOne(self, digits):
        i = len(digits) - 1
        while i >= 0:
            if 0 <= digits[i] <= 8:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
                if i == 0:
                    digits = [1] + digits
                    return digits
            i -= 1