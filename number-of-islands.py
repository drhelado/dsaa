class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])

        # visited = [] # list returns time limit exceeded
        visited = set()

        islands = 0

        def dfs(r, c):
            stack = []
            # stack = deque()

            coordinate = (r, c)

            # visited.append(coordinate)
            visited.add(coordinate)
            stack.append(coordinate)

            while stack:
                row, col = stack.pop()
                # row, col = stack.popleft()

                # right left top bottom
                # directions = { 'right': {1, 0}, 'left': {-1, 0}, 'top': {0, -1}, 'bottom': {0, 1} }
                directions = [ [1,0], [-1,0], [0,-1], [0,1] ]

                for dr, dc in directions:
                    r, c = row + dr, col + dc

                    if r in range(rows) and c in range(cols) and grid[r][c] == '1' and (r, c) not in visited:
                        stack.append((r, c))
                        # visited.append((r, c))
                        visited.add((r, c))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    dfs(r, c)
                    islands += 1

        return islands
