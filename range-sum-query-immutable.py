class NumArray:

    def __init__(self, nums: List[int]):
        self.dp = [0] + list(accumulate(nums))

    def sumRange(self, left: int, right: int) -> int:
        return self.dp[right + 1] - self.dp[left]  
