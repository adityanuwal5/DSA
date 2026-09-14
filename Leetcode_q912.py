
class Solution(object):
    def sortArray(self, nums):
        self.nums = nums
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        return self.mearge(left,right)
    def mearge(self, left, right):
        i = 0
        j = 0
        mix = []
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                mix.append(left[i])
                i += 1
            else:
                mix.append(right[j])
                j += 1
        while i < len(left):
            mix.append(left[i])
            i += 1
        while j < len(right):
            mix.append(right[j])
            j += 1
        return mix
