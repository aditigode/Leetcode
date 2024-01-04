class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.tokenList = {}
        

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokenList[tokenId] = currentTime
        

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.tokenList and self.timeToLive + self.tokenList[tokenId] > currentTime:
            self.tokenList[tokenId] = currentTime
        

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        for time in self.tokenList.values():
            if time + self.timeToLive > currentTime:
                count += 1
        return count
        
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)