class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:

        output = []

        # there should be enough elements to be divided in rows and cols
        if len(original) != m * n:
            return output

        for i in range(m):
            # get starting and ending index for row
            s = i * n
            e = s + n
            row = original[s:e]

            output.append(row)

        return output
