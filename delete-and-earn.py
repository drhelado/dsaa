class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:

        count = Counter(nums)
        nums = sorted(list(set(nums)))
        # nums = sorted(list(nums)) # wrong answer

        # print(nums)
        # print(nums1)

        earn1, earn2 = 0, 0
        for i in range(len(nums)):
            v = nums[i]
            curEarn = v * count[v]

            # can't use both earn1 and eran2
            if i > 0 and v == nums[i - 1] + 1:
                temp = earn2
                earn2 = max(curEarn + earn1, earn2)
                earn1 = temp
            else:
                temp = earn2
                earn2 = curEarn + earn2
                earn1 = temp

        return earn2
