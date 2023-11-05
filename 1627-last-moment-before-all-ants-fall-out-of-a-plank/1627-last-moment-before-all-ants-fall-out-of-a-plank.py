class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        if left:
            max_left = max(left)
        else:
            return n - min(right)
            
        if right:
            min_right = min(right)
        
        else:
            return max_left
        
        return max(max_left, n-min_right)
        