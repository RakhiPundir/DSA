class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        f = 0
        s = 0
        while(f < len(nums)):
            while(f < len(nums)) and (nums[f] == nums[s]):
                f += 1
            if f == len(nums):
                return s+1
            s += 1
            nums[s] = nums[f]
        return s+1
