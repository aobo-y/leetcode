#
# @lc app=leetcode id=355 lang=python3
#
# [355] Design Twitter
#

# @lc code=start
from collections import defaultdict, deque
import heapq
class Twitter:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.follows = defaultdict(set)
        self.tweets = defaultdict(deque)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1
        if len(self.tweets[userId]) > 10:
            self.tweets[userId].popleft()

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        heap = []
        heapq.heapify(heap)

        for u in {userId} | self.follows[userId]:
            for t in self.tweets[u]:
                heapq.heappush(heap, t)
                if len(heap) > 10:
                    heapq.heappop(heap)

        feeds = []
        while heap:
            feeds.append(heapq.heappop(heap)[1])

        return feeds[::-1]


    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.follows[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# @lc code=end

