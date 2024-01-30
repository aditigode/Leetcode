#1 2 3 4
#5 6 7 8
#4 3 2 1 

class MyQueue:

    def __init__(self):
        self.stack = []
        self.stackV2 = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        
        
        

    def pop(self) -> int:
        if not self.stackV2:
            while len(self.stack) > 1:
                self.stackV2.append(self.stack.pop())
            return self.stack.pop()
        else:
            return self.stackV2.pop()
        

    def peek(self) -> int:
        if not self.stackV2:
            while self.stack:
                self.stackV2.append(self.stack.pop())
        return self.stackV2[-1]
        

    def empty(self) -> bool:
        #print(self.stack, self.stackV2)
        return not self.stack and not self.stackV2
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()