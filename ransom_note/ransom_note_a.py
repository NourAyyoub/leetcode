class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        if len(ransomNote) > len(magazine):
            return False
        else:
            while len(ransomNote) > 0:
                if (ransomNote.count(ransomNote[0])) > (magazine.count(ransomNote[0])):
                    return False
                ransomNote = ransomNote.replace(ransomNote[0],'')
            return True 