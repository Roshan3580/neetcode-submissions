class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list) # userid: tweets
        self.follows = defaultdict(set) # user 1 follows user 2 (user1:user2)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([-self.time, tweetId])
        if len(self.tweets[userId]) > 10:
            self.tweets[userId].pop(0)
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []
        tweets += self.tweets[userId]
        res = []
        for followee in self.follows[userId]:
            tweets += self.tweets[followee]
        heapq.heapify(tweets)

        while tweets and len(res) < 10:
            time, tweetId = heapq.heappop(tweets)
            res.append(tweetId)

        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follows[followerId].add(followeeId)
    
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
