class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num = sorted(nums)
        i = 0
        while(i <= len(num)):
            if(i == len(num)-1):
                return num[i]
            else:
                if(num[i] == num[i+1]):
                    i += 2
                else:
                    return num[i]
