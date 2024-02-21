class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # 101 110 111 = 1 0 0
        # 5 6 7
        shift = 0
        while left < right:
            #do right shift by position
            left >>= 1
            right >>= 1
            shift += 1
        #move the left with as many positions as you shifted right previously
        return left << shift
        