class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        # print(heights)

        rows = len(heights)
        cols = len(heights[0])

        pacific = []
        atlantic = []

        def dfs(row, col, visited, prevHeight):



            coordinate = (row, col)

            if coordinate in visited:
                return

            row_out_of_bound = row < 0 or row == rows
            col_out_of_bound = col < 0 or col == cols

            if row_out_of_bound or col_out_of_bound:
                return

            height = heights[row][col]
            shorter_than_prev = height < prevHeight

            # if coordinate in visited or row_out_of_bound or col_out_of_bound or shorter_than_prev:
            if shorter_than_prev:
                return

            # print('row, col, visited, prevHeight', (row, col, visited, prevHeight))

            visited.append(coordinate)

            dfs(row + 1, col, visited, height)
            dfs(row - 1, col, visited, height)
            dfs(row, col + 1, visited, height)
            dfs(row, col - 1, visited, height)


            # print('visited', (visited))




        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])

        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])


        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])

        return res
