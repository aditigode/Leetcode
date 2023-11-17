class Solution:
    def myPow(self, x: float, n: int) -> float:
        @cache
        def recurse(x,n):
            if n==1:
                return x
            elif n==-1:
                return 1/x
            elif n==0:
                return 1
            

            return recurse(x,n//2) * recurse(x,n//2) * recurse(x,n%2)
        return recurse(x,n)
            
