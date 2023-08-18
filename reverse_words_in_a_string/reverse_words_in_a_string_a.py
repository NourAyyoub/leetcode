class Solution(object):
    def reverseWords(self, s):
        w = s.split()
        w.reverse()
        w = " ".join(w)
        return w