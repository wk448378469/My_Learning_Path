from collections import defaultdict
import heapq


class Solution(object):
    def networkDelayTime(self, times, N, K):
        # build graph
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        pq = [(0, K)]
        dist = {}
        while pq:
            d, node = heapq.heappop(pq)
            if node in dist: continue
            dist[node] = d
            for nei, d2 in graph[node]:
                if nei not in dist:
                    heapq.heappush(pq, (d+d2, nei))

        return max(dist.values()) if len(dist) == N else -1

    def networkDelayTime2(self, times, N, K):
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((w, v))

        dist = {node: float('inf') for node in range(1, N+1)}

        def dfs(node, elapsed):
            if elapsed >= dist[node]: return
            dist[node] = elapsed
            for time, nei in sorted(graph[node]):
                dfs(nei, elapsed + time)

        dfs(K, 0)
        ans = max(dist.values())
        return ans if ans < float('inf') else -1


if __name__ == '__main__':
    s = Solution()
    print(s.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))
    print(s.networkDelayTime2([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))
