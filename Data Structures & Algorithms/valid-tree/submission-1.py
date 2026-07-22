class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n-1:
            return False
        adj = defaultdict(list)
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)

        visit = set()

        def dfs(node, root):
            if node in visit:
                return False
            visit.add(node)
            for nei in adj[node]:
                if nei == root:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        
        return dfs(0, -1) and len(visit) == n
        