from collections import defaultdict
class Twitter:

    def __init__(self):
        self.newsfeeds = defaultdict(list) # userid , list tweets
        self.followers = defaultdict(set)
        self.time = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.newsfeeds[userId], (self.time, tweetId))
        self.time += 1
        while len(self.newsfeeds[userId]) > 10:
            heapq.heappop(self.newsfeeds[userId])
        

    def getNewsFeed(self, userId: int) -> List[int]:
        newsfeeds = [self.newsfeeds[followerOf] for followerOf in self._getWhoIFollow(userId)]
        newsfeeds.append(self.newsfeeds[userId])
        newsfeeds = sum(newsfeeds, [])
        top10 = heapq.nlargest(10, newsfeeds)
        top10 = [ x[1] for x in top10] 
        return top10
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followeeId].add(followerId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers[followeeId]:
            self.followers[followeeId].remove(followerId)
                      
    def _getWhoIFollow(self, userId: int):
        result = set()
        for user in self.followers:
            if userId in self.followers[user]:
                result.add(user)
        return result                  
    


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)