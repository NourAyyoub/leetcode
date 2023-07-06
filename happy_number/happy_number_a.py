class Solution(object):
    def sum_of_square(self, s):
        x = 0
        for i in s:
           x += int(i) ** 2
        return x

    def isHappy(self, n):
        arr = []
        c = self.sum_of_square(str(n))
        while True:
          if c == 1:
            return True
          elif c in arr:
              return False
          else:
              arr.append(c)
              c = self.sum_of_square(str(c))

