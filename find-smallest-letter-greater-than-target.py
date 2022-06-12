class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        n = len(letters)

        if letters[n - 1] <= target or letters[0] > target:
            return letters[0]

        l, r = 0, n - 1

        while l + 1 < r:

            # find middle
            # m = l + (r - l) // 2
            m = (r + l) // 2

            # if target == letters[m]:
                # return letters[m]
            if target < letters[m]:
                r = m
            elif target >= letters[m]:
                l = m

        return letters[r]
