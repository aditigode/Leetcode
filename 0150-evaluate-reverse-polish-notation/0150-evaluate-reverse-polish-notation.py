class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        if len(tokens) == 1:
            return int(tokens[0])
        
        for i in range(len(tokens)):
            if tokens[i].isdigit() or tokens[i][1:].isdigit():
                stack.append(tokens[i])
            else:
                op2 = int(stack.pop())
                op1 = int(stack.pop())
                #print("op1",op1)
                #print("op2",op2)
                #print("token",tokens[i])
                if tokens[i] == "+":
                    res = op1 + op2


                elif tokens[i] == "-":
                    res = op1 - op2
                    
                elif tokens[i] == "*":
                    res = op1 * op2
                elif tokens[i] == "/":
                    res = int(op1 / op2)
                    
                stack.append(res)
                #print(stack)
        #print(stack)
        return stack[0]
                
        
        