class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        num = sorted(nums)
        n = len(num)
        sol = []
        j = -1
        while(j+n != 0):
            for i in range(j+n):
                for k in range(i+1, j+n):
                    op = []
                    if(num[j] + num[i] + num[k] == 0):
                        op.append(num[i])
                        op.append(num[k])
                        op.append(num[j])
                        sol.append(op)
            j -= 1
        soln = []
        for i in sol:
            if i not in soln:
                soln.append(i)
        
        return soln    
