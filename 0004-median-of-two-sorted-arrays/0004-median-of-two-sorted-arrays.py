class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
            
        half = (len(nums1)+len(nums2))//2
        
        i,j = 0, len(nums1)-1
        #odd length
        if (len(nums1)+ len(nums2)) % 2 != 0:
            length = 'odd'
        #even length
        else:
            length = 'even'
            
        while True:
            mid1 = (i+j) // 2
            
            mid2 = half - mid1 - 2
            
            #print(mid1,mid2)
            nums1_left = nums1[mid1] if mid1 >= 0 else float('-infinity')
            nums1_right = nums1[mid1+1] if (mid1+1) < len(nums1) else float('infinity')
            nums2_left = nums2[mid2] if mid2 >= 0 else float('-infinity')
            nums2_right = nums2[mid2 +1] if (mid2+1) < len(nums2) else float('infinity')
            
            if nums1_left > nums2_right:
                j = mid1-1
            elif nums1_right < nums2_left :
                i = mid1+1
            else:
                if length == 'even':
                    median = (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
                else:
                    #print("odd",nums1_right, nums2_right)
                    median = min(nums1_right, nums2_right)
                return median
            
        
        
        