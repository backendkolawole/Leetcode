class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        columns = len(heights[0])
        pacific = set()
        atlantic = set()
        result = []

        def dfs(r, c, visited, prevHeight):
            if ((r, c) in visited or r < 0 or c < 0 or r == rows or c == columns or heights[r][c] < prevHeight):
                return 
            # print(f"cell: {heights[r][c]}, row: {r}, column : {c}, prevHeight: {prevHeight}")
            visited.add((r, c))
            dfs(r - 1, c, visited, heights[r][c]) # up
            dfs(r, c + 1, visited, heights[r][c]) # right
            dfs(r + 1, c, visited, heights[r][c]) # down
            dfs(r, c - 1, visited, heights[r][c]) # left


        for j in range(columns):
            dfs(0, j, pacific, heights[0][j])
            dfs(rows - 1, j, atlantic, heights[rows - 1][j])

        for i in range(rows):
            dfs(i, 0, pacific, heights[i][0])
            dfs(i, columns - 1, atlantic, heights[i][columns -1])

        for i in range(rows):
            for j in range(columns):
                if (i, j) in pacific and (i, j) in atlantic:
                    result.append([i, j])

        return result
        