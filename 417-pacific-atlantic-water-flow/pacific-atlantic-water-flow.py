class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        pacVisited = set()
        atlVisited = set()
        rows, cols = len(heights), len(heights[0])

        def dfs(r, c, visited, preHeight):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visited or heights[r][c] < preHeight:
                return
            
            visited.add((r, c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        for r in range(rows):
            dfs(r, 0, pacVisited, heights[r][0])
            dfs(r, cols - 1, atlVisited, heights[r][cols - 1])

        for c in range(cols):
            dfs(0, c, pacVisited, heights[0][c])
            dfs(rows - 1, c, atlVisited, heights[rows - 1][c])

        res = []

        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacVisited and (r, c) in atlVisited:
                    res.append((r, c))
        
        return res
        
