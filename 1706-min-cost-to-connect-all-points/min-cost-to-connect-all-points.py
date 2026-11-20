class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = {i:[] for i in range(n)}
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        visited = set()
        minHeap = [[0, 0]]
        res = 0

        while minHeap:
            dist, node = heapq.heappop(minHeap)
            if node in visited:
                continue
    
            visited.add(node)
            res += dist

            for neiDist, neiNode in adj[node]:
                if neiNode not in visited:
                    heapq.heappush(minHeap, [neiDist, neiNode])
        
        return res