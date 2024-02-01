class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        
        nums.sort()
        # 1 1 3 3 4 5 7 8 9
        # 1 1 3
        # 1 2 3 3 3 7
        # 1 2 3 3 3 7
        answer = []
        temp = []
        count = 0
        #prev, prevprev =nums[0], nums[0]
        for i in range(len(nums)):
            if count == 3:
                answer.append(temp)
                temp = []
                count = 0
            for j in range(len(temp)):
                if nums[i] - temp[j] > k:
                    return []
            temp.append(nums[i])
            count += 1
        answer.append(temp)
        return answer
                
            
                
                    
            
        