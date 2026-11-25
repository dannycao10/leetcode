class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        minHeap = [[0, 0, 0]]
        visited = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while minHeap:
            diff, r, c = heapq.heappop(minHeap)
            if (r, c) in visited:
                continue
            
            if (r, c) == (rows - 1, cols - 1):
                return diff

            visited.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols or (nr, nc) in visited:
                    continue
                newDiff = max(diff, abs(heights[nr][nc] - heights[r][c]))
                heapq.heappush(minHeap, [newDiff, nr, nc])