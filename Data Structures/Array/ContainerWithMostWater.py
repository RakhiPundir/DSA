class Solution:
    def maxArea(self, height: List[int]) -> int:
        #n = len(height)
        #li = []
        #for i in range(n):
        #    k = 0
        #    for j in range(i+1, n):
        #        k += 1
        #        p = min(height[i],height[j]) * k
        #        li.append(p)
        #print(li)
        #return max(li)
        left, right, max_amount = 0, len(height)-1, 0
    
        while left < right:
            max_amount = max(max_amount, (right-left)*min(height[left],height[right]))

            if height[left] <= height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1

        return max_amount
