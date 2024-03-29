class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left,right = 0,0
        # 1 2 3 1 2 3 1 2 ; k = 2
        # [1: 2, 2: 2, 3: 3] , record max and move the window
        
        freq_dict = {}
        
        #print(freq_dict)
        maxLength = 0
        
        while right < len(nums):
            if nums[right] in freq_dict:
                freq_dict[nums[right]] += 1
                
            else:
                freq_dict[nums[right]] = 1
                
            # this code is to reduce left window until the condition k is satisfied on the right window
            while freq_dict[nums[right]] > k:
                #print(freq_dict, left, right)
                freq_dict[nums[left]] -= 1
                left += 1
            #print(maxLength, right-left+1)
            maxLength = max(maxLength, (right-left+1))
            right += 1
                
        return maxLength
                    
            
       
                
                
                    
                    
            
            
        