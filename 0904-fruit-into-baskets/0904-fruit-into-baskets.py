class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # sliding window
        basketSize = 0
        left,right = 0,0
        type = {}
        longest = 0
        
        while right < len(fruits):
            #update the lastest index where the type of fruit encountered
            
            type[fruits[right]] = right
            
            #if basket not full
            if len(type) > 2:
                
                ptr = math.inf
                discardType = ""
                # discard the type of fruit with min index to cover max fruits
                for key,val in type.items():
                    if ptr > val:
                        ptr = val
                        discardType = key
                del type[discardType]
                #update the left window to reduce the window size and discard a fruit type
                #print(left, discardType)
                left = ptr+1
                
              
                
            
            #print(left,right, longest)
            longest = max(longest, right-left+1)
            # increase the right window size
            right += 1
        return longest
                
                
                
                
            
            
        
        
        