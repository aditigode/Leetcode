# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        def find_peak():
            low, high = 0, mountain_arr.length() - 1
            while low <= high:
                mid = (low + high) // 2
                leftval, midval, rightval = mountain_arr.get(mid-1), mountain_arr.get(mid),mountain_arr.get(mid+1)
                if leftval < midval and midval < rightval:
                    low = mid
                elif leftval > midval and midval > rightval:
                    high = mid
                elif leftval < midval and midval > rightval:
                    return mid
            return -1

        
        def find_left_mountain(low, high, target):
            while low <= high:
                mid = (low + high) // 2
                midval = mountain_arr.get(mid)
                if midval < target:
                    low = mid + 1
                elif midval > target:
                    high = mid - 1
                elif midval == target:
                    return mid
            return -1

        def find_right_mountain(low, high, target):
            while low <= high:
                mid = (low + high) // 2
                midval = mountain_arr.get(mid)
                if midval > target:
                    low = mid + 1
                elif midval < target:
                    high = mid - 1
                elif midval == target:
                    return mid
            return -1

        peak_idx = find_peak()
        #print(peak_idx)
        left_idx = find_left_mountain(0, peak_idx, target)
        if left_idx < 0:
            return find_right_mountain(peak_idx, mountain_arr.length()- 1,target)
        else:
            return left_idx
            

                

        