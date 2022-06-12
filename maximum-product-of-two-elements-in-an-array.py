class Solution:
    def maxProduct(self, nums: List[int]) -> int:


        # print(nums)

        heap = []

        for i in nums:
            heappush(heap, -1 * i)

        out = []

        while heap:

            i = -1 * heappop(heap)

            out.append(i)

            if len(out) == 2:
                break

            print(i)

        print(out)


        print(heap)


        return (out[-1] - 1) * (out[-2] - 1)
