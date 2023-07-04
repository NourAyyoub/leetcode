class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        if len(ransomNote) > len(magazine):
            return False
        else:
            for i in ransomNote:
                if (ransomNote.count(i)) > (magazine.count(i)):
                    return False
            return True False