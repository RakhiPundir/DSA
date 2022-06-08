class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left, partial_sum, max_avg_sum = 0, 0, -float("inf")
        for right in range(len(nums)):
            partial_sum += nums[right]
            if right - left + 1 == k:
                max_avg_sum = max(max_avg_sum, partial_sum / k)
                partial_sum -= nums[left]
                left += 1
        return max_avg_sum
