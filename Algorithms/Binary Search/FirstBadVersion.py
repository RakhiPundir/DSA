class Solution:
    def firstBadVersion(self, n: int) -> int:
        first, last = 1, n
		
        while first <= last:
            middle = (first + last) // 2
            if isBadVersion(middle) is True and isBadVersion(middle - 1) is False:
                return middle
            if isBadVersion(middle) is False:
                first = middle + 1
            else:
                last = middle - 1
