class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        j = -1
        if target in nums:
            for i in range(n):
                if(nums[i] == target):
                    return i
                elif(nums[j] == target):
                    return (n+j)
                j -= 1
        else:
            for i in range(n):
                if(nums[i] < target):
                    if(i+1 == n):
                        return n
                    else:
                        if(nums[i+1] > target):
                            return i+1
                elif(nums[0] > target):
                    return 0
