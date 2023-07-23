class Solution(object):
    def searchInsert(self, nums, target):
        f, s = 0, len(nums) - 1
        while f <= s:
            t = (f + s) // 2
            if nums[t] == target:
                return t
            elif nums[t] < target:
                f = t + 1
            else:
                s = t - 1
        return f