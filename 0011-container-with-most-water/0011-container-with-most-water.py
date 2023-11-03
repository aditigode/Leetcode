class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
        i, j = 0, len(height)-1
        while i < j:
            maxarea = max(maxarea, ((j-i) * min(height[i], height[j])))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
            
        return maxarea

        