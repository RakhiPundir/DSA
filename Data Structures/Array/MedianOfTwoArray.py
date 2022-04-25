class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        print(nums)
        n = len(nums)
        if(n%2 == 0):
            median = (nums[int(n/2)] + nums[int(n/2) - 1])/2
            return median
        else:
            return float(nums[n//2])
