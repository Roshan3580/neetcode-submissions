class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edge_cost = defaultdict(list)
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i+1, len(points)):
                x2, y2 = points[j]
                cost = abs(x1 - x2) + abs(y1 - y2)
                edge_cost[i].append((cost, j))
                edge_cost[j].append((cost, i))
        res = 0
        mini = [[0,0]]
        visit = set()
        while len(visit) < len(points):
            cost, node = heapq.heappop(mini)
            if node in visit:
                continue
            res += cost
            visit.add(node)
            for neiCost, nei in edge_cost[node]:
                if nei not in visit:
                    heapq.heappush(mini,[neiCost, nei])
        return res