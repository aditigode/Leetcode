class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # 2 / 1 == 0 [1,2]
        # 4 / 1 == 0 [4 1]
        # 2**n brute force
        # 1 3 4 8 = dp[]
        # 3 1 4 8 = null 1, null,null, 1 3, 1, null, 1 ,  
        # i, 1
        # 0, 1 = 1,1 [1,2]= 2,1 2,1
        # 0, 0 = 1,2 [2] = 2,2 [2] 2,0
       # The container that holds all intermediate solutions.
        # key: the largest element in a valid subset.
        # time complexity O(N^2)
        subsets = {-1: set()}
        
        for num in sorted(nums):
            subsets[num] = max([subsets[k] for k in subsets if num % k == 0], key=len) | {num}
            #print(subsets)
        
        return list(max(subsets.values(), key=len))
    
   
            
        