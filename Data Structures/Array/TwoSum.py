class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sol = []
        j = -1
        for i in range(len(nums)):
            if(nums[i] + nums[j] == target):
                sol.append(i) 
                sol.append(len(nums)+j)
                return sol
            else:
                for j in range(-1, -(len(nums)-i+1), -1):
                    if(nums[i] != nums[j]):
                        if(nums[i] + nums[j] == target):
                            sol.append(i) 
                            sol.append(len(nums)+j)
                            return sol
                    elif(nums[i] == nums[j]):
                        continue
