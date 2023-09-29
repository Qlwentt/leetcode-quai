from collections import defaultdict
class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.userFollows = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        self.follow(userId, userId)
        newsFeedTweets = []
        for personIFollow in self.userFollows[userId]:
            newsFeedTweets.extend(self.tweets[personIFollow])
        answer =  heapq.nlargest(10, newsFeedTweets, key=itemgetter(0) )
        answer = [tweet for time, tweet in answer]
        return answer
        
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.userFollows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.userFollows[followerId]:
            self.userFollows[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)