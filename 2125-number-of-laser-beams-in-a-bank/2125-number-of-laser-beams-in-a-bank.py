class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prevBeamCount = 0
        beams = 0
        for i in range(len(bank)):
            currBeamCount = 0
            for j in range(len(bank[0])):
                if bank[i][j] == '1':
                    currBeamCount += 1
            if prevBeamCount > 0 and currBeamCount > 0:
                beams = beams + (prevBeamCount * currBeamCount)
            if currBeamCount > 0:
                prevBeamCount = currBeamCount
        return beams
                
                    
        