class Solution:
    def convert(self, s: str, numRows: int) -> str:

        
        if numRows <= 1:
            return s

        l = len(s)

        arr = ["" for x in range(l)]

        row = 0

        for i in range(l):

            arr[row] += s[i]

            # when last row reached, start moving up
            if row == numRows -1:
                down = False
            # when first row is reached, start moving down
            elif row == 0:
                down = True

            if down:
                row += 1
            else:
                row -= 1

        result = ""

        for i in range(numRows):
            if i < len(s):
                result += arr[i]
            # print(arr[i], end = "")

        return result
