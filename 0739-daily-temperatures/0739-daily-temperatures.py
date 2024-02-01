class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
       
        
        #  73,2 74,3 75,5 76,9
        
        # 30,2 40,3 50,4 60,5
        
        # monotonically decreasing stack/next greater element
        stack = []
        answer = [0] * len(temperatures)
        for i in range(len(temperatures)-1,-1,-1):
            while stack and stack[-1][1] <= temperatures[i]:
                stack.pop()
            if stack:
                daysPassed = stack[-1][0] - i
                answer[i] = daysPassed
            stack.append((i,temperatures[i]))
        return answer