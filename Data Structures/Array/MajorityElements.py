class Solution:
    def majorityElements(self, nums: List[int]) -> int:
      l = len(nums)//2
      dic = {}
      for i in nums:
        if i not in dic:
          dic[i] = 1
        else:
          dic[i] += 1
        if dic[i]>1:
          return i
      return
