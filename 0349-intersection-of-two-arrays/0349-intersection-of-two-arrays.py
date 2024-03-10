class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        nums1.sort()
        nums2.sort()
        i,j = 0,0
        print(nums1,nums2)
        result = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1
                
                
            elif nums1[i] < nums2[j] :
                i += 1
                
            else:
                j += 1
        return result