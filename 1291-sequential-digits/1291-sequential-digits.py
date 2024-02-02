class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        window ="123456789"
        result = []
        for i in range(len(str(low)),len(str(high))+1):
            for j in range(10-i):
                num = int(window[j:j+i])
                if low <= num <= high:
                    result.append(num)
        return result
