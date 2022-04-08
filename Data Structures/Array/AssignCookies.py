class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        ans=0
        i=0
        for j in range(len(s)):
            if(i<len(g) and s[j]>=g[i]):
                ans+=1
                i+=1
        return ans
