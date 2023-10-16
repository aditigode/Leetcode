class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev, curr = [],[]
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        if rowIndex == 2:
            return [1,2,1]
        prev = [1,2,1]

        counter = 3
        while counter <= rowIndex:
            #add one of both sides
            curr = [0] * (counter+1)
            mid = len(prev)//2
            i = 0
            counter += 1
            while i < len(prev)-1:
                #print(prev, curr, i)
                curr[i+1] = prev[i] + prev[i+1]
                i += 1
            curr[0] = 1
            curr[-1] = 1
            prev = curr
            
            
        return curr
                


            #counter += 1

        