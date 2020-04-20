#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#

# @lc code=start
import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.mid = None
        self.left = [] # max q
        self.right = [] # min q

    def addNum(self, num: int) -> None:
        if self.mid is None:
            if not self.left:
                self.mid = num
            elif num < - self.left[0]:
                self.mid = - heapq.heappushpop(self.left, -num)
            elif num > self.right[0]:
                self.mid = heapq.heappushpop(self.right, num)
            else:
                self.mid = num
        else:
            if num > self.mid:
                heapq.heappush(self.right, num)
                heapq.heappush(self.left, -self.mid)
            else:
                heapq.heappush(self.right, self.mid)
                heapq.heappush(self.left, -num)

            self.mid = None


    def findMedian(self) -> float:
        return self.mid if self.mid else (- self.left[0] + self.right[0]) / 2



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

