class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_dict = collections.Counter(nums)
        for num,count in nums_dict.items():
            if count > len(nums)//2:
                return num
        