class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        else:
            while len(s) > 0:
                if (s.count(s[0])) != (t.count(s[0])):
                    return False
                s = s.replace(s[0], '')
            return True