class ListNode:
    def __init__(self, userID=-1,tweetID=-1):
        self.userID = userID
        self.tweetID = tweetID
        self.next = None
        
class Twitter:

    def __init__(self):
        self.tweetList = ListNode()
        self.users = {}
        
    
    def creatUser(self, userId):
        self.users[userId] = [userId]
        
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        head = self.tweetList
        if userId not in self.users:
            self.creatUser(userId)
        
        newTweet = ListNode(userId, tweetId)
        newTweet.next = head.next
        head.next = newTweet
        
        
        
        

    def getNewsFeed(self, userId: int) -> List[int]:
        head = self.tweetList
        if userId not in self.users:
            self.creatUser(userId)
        followers = self.users[userId]
        resultTweetIDs = []
        count = 0
        while head and count < 10:
            if head.userID in followers:
                resultTweetIDs.append(head.tweetID)
                count += 1
            head = head.next
        return resultTweetIDs
        

    def follow(self, followerId: int, followeeId: int) -> None:
        head = self.tweetList
        if followerId not in self.users:
            self.creatUser(followerId)
        self.users[followerId].append(followeeId)
        
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)