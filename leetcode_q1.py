# class Solution(object):
#     def twoSum(self, nums, target):
#         num_dict = {}
#         for i, num in enumerate(nums):
#             complement = target - num
#             if complement in num_dict:
#                 return (num_dict[complement], i)
#             num_dict[num] = i
#         return None

# Another approach using two pointers
class Solution(object):
    def twoSum(self, nums, target):
        num_dict = {}
        # Loop through indices from 0 to the length of the list
        for i in range(len(nums)):
            num = nums[i]  # Fetch the value manually using the index
            complement = target - num    
            if complement in num_dict:
                return (num_dict[complement], i)
            num_dict[num] = i
        return None


