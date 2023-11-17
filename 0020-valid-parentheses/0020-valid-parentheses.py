class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] in ['(','[','{']:
                stack.append(s[i])
            elif s[i] == ')' and stack and stack[-1]=='(':
                stack.pop()
            elif s[i] == ']' and stack and stack[-1]=='[':
                stack.pop()
            elif s[i] == '}' and stack and stack[-1]=='{':
                stack.pop()
            else:
                #print("Else")
                return False
        return False if stack else True
                
        