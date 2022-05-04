class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        s = 0
        num = sorted(nums)
        for i in range(0,len(num)-1,2):
            s += num[i]
        return s
