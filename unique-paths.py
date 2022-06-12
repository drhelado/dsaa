class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # grid = [[1] * n] * n
        row = [1] * n

        # print(grid)

        for i in range(m - 1):
            _row = [1] * n
            for j in range(n - 2, -1, -1):
                # grid[i][j] = grid[i][j + 1] + grid[i][j]
                _row[j] = _row[j + 1] + row[j]

                print(row)
                print(_row)

            row = _row

        # return grid[0][0]
        return row[0]
