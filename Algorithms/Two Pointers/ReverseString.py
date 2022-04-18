class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        j = -1
        for i in range(n//2):
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            j -= 1
            #print(s)
