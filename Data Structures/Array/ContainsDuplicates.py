class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in nums:
            if(nums.count(i) >= 2):
                return True
            else:
                continue
        return False
