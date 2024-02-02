class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        window ="123456789"
        
        result = []
        for i in range(len(str(low)),len(str(high))+1):
            # 10-i to is adjust for the last window. Eg: if len(low)=3 last window should be 7:7+3= 7:10: 789
            # 10-i will prevent index out of range error
            for j in range(10-i):
                num = int(window[j:j+i])
                if low <= num <= high:
                    result.append(num)
        return result
