class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum1=0
        n=len(nums)
        sum1=n*(n+1)//2
        sum2=sum(nums)
        return sum1-sum2
