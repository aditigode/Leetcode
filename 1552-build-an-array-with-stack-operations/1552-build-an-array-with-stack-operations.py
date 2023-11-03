class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        i, j = 0,1
        stack = []

        while j <= n+1:
            if target[i] == j:
                stack.append("Push")
                if i == len(target) -1:
                    break
                i += 1
            
            else:
                stack.append("Push")
                stack.append("Pop")
            j += 1
        print(stack)
        return stack

        