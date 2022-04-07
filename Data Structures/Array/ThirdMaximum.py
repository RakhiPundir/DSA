class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        sortedArray = list(sorted(set(nums)))
        if(len(sortedArray)>=3):
            return sortedArray[-3]
        elif(len(sortedArray)<=2):
            return sortedArray[-1]    
