class MedianFinder:

    def __init__(self):

        self.small = [] # maxheap
        self.large = [] # minheap

    def addNum(self, num: int) -> None:

        heappush(self.small, -1 * num)

        # print(self.small)
        # print(self.large)


        if self.small and self.large:
            if -1 * self.small[0] > self.large[0]:
                valueToBeMoved = -1 * heappop(self.small) # change to positive value before moving to minheap
                heappush(self.large, valueToBeMoved)

        if len(self.small) > len(self.large) + 1:
            valueToBeMoved = -1 * heappop(self.small) # change to positive value before moving to minheap
            heappush(self.large, valueToBeMoved)

        if len(self.large) > len(self.small) + 1:
            valueToBeMoved = heappop(self.large)
            heappush(self.small, -1 * valueToBeMoved)


        # heappush(self.top, -heappop(self.bot))

        # if len(self.top) > len(self.bot):
            # heappush(self.bot, -heappop(self.top))

    def findMedian(self) -> float:

        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]

        return (-1 * self.small[0] + self.large[0]) / 2

        # if len(self.bot) != len(self.top):
        #     return -self.bot[0]
        # else:
        #     return (self.top[0] - self.bot[0]) / 2



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
