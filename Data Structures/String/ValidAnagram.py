class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sa = sorted(s)
        ta = sorted(t)
        n = 0
        if(len(sa) == len(ta)):
            for i in range(len(sa)):
                if(sa[i] == ta[i]):
                    n += 1
                else:
                    return False
            if(n == len(sa)):
                return True
        else:
            return False
