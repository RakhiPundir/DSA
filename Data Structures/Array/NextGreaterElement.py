class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                insert_value = -1
                start_index = nums2.index(nums1[i])
                for j in range(start_index, len(nums2)):
                    if j < len(nums2)-1 and nums2[j+1] > nums2[start_index]:
                        insert_value = nums2[j+1]
                        break
                ans.append(insert_value)
            else:
                ans.append(-1)
        return ans
