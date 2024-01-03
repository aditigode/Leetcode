class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        i = 0
        row = 0
        array = []
        while True:
            nums_set = set()
            i = 0
            rows_needed = True
            rows = []
            while i < len(nums):
                if nums[i] != 0 and nums[i] not in nums_set:
                    rows_needed = False
                    nums_set.add(nums[i])
                    rows.append(nums[i])
                    nums[i] = 0
                i += 1
            row += 1
            array.append(rows)
            if rows_needed:
                array.pop()
                break
        return array
                    
        