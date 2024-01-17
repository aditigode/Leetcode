class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arrayOccur = {}
        OccurSet = set()
        
        for num in arr:
            if num not in arrayOccur:
                arrayOccur[num] = 0
            arrayOccur[num] += 1
            
        for num, count in arrayOccur.items():
            prevLength = len(OccurSet)
            OccurSet.add(count)
            if prevLength == len(OccurSet):
                return False
            
        return True