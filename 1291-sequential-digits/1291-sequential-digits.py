class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        # approach 1 : using deque
        q = collections.deque([i for i in range(1,10)])
        result = []
        while q:
            #print(q)
            num = q.popleft()
            if low <= num <= high:
                result.append(num)
            
            lastDigit = num % 10
            if lastDigit + 1 < 10:
                q.append(num*10 + lastDigit+1)
        return result
                
        
#         #approach 2
#         window ="123456789"
        
#         result = []
#         for i in range(len(str(low)),len(str(high))+1):
#             # 10-i to is adjust for the last window. Eg: if len(low)=3 last window should be 7:7+3= 7:10: 789
#             # 10-i will prevent index out of range error
#             for j in range(10-i):
#                 num = int(window[j:j+i])
#                 if low <= num <= high:
#                     result.append(num)
#         return result
