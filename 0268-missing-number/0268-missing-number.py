class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        current = 0
        for num in nums:
            if current != num:
                return current
            current += 1
        return current
        