class Solution:



    def orangesRotting(self, grid: List[List[int]]) -> int:

        def bfs(q):

            weight = 0

            while len(q) != 0:
                i, j, minutes = q.popleft()

                weight = max(minutes, weight)

                for new_i, new_j in [(1,0), (0, 1), (-1, 0), (0, -1)]:
                    new_i, new_j = i + new_i, j + new_j
                    if new_i >= 0 and new_i < len(grid) and new_j >= 0 and new_j < len(grid[0]) and grid[new_i][new_j] == 1:
                        grid[new_i][new_j] = 2
                        q.append((new_i, new_j, minutes + 1))

            return weight


        q = collections.deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j, 0))

        minutes = bfs(q)

        for row in grid:
            if 1 in row:
                return -1

        return minutes
