class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # gas = [1,2,3,4,5]
        # cost = [3,4,5,1,2]
        # start at station 3 
        # tank at st 3= 0+4= 4
        # tant at st 4=4-1+5= 8
        # tank at st 0= 8-2+1= 7
        # tank at st 1= 7-3+2=6
        # tank at st 2= 6-4+3=5
        # spend 4 to arrive at st 3 again
        if sum(gas) < sum(cost): return -1
        currentGain, totalGain = 0, 0
        startIndex = 0
        for i in range(len(gas)):
            totalGain += gas[i] - cost[i]
            currentGain += gas[i] - cost[i]

            if currentGain < 0:
                startIndex = i +1
                currentGain = 0
        #print(totalGain)
        return startIndex if totalGain >= 0 else -1

        


        