class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        candy = set(candyType)
        c = len(candy)
        ct = len(candyType)
        if(c < ct/2):
            return c
        else:
            return ct//2
