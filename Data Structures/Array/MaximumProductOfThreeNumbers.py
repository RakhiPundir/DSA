class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        li = sorted(nums)
        return max(li[-1]*li[-2]*li[-3],li[0]*li[1]*li[-1])
