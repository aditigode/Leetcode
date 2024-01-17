class RandomizedSet:

    def __init__(self):
        # dict for storing values and indices of list with the same values
        self.randomDict = {}
        # list for random choice
        self.lst = []
        

    def insert(self, val: int) -> bool:
        if val in self.randomDict:
            return False
        
        # O(1)
        self.lst.append(val)
        # O(1)
        self.randomDict[val] = len(self.lst) - 1
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.randomDict:
            return False
        
        #remove the index
        index = self.randomDict[val]
        #make the last element of list ready for popping to get O(1) complexity. save the value first
        self.lst[index] = self.lst[-1]
        self.randomDict[self.lst[-1]] = index
        
        #O(1)
        self.lst.pop()
        # O(1)
        del self.randomDict[val]
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.lst)
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()