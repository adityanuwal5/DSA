class Solution(object):
    def containsDuplicate(self, nums):
        num_dict = {}
        for num in nums:
            if num in num_dict:
                return True
            num_dict[num] = 1
        return False