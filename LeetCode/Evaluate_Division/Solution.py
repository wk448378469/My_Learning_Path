from collections import defaultdict


class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = defaultdict(list)
        weight = defaultdict(list)
        for (molecule, denominator), v in zip(equations, values):
            graph[molecule].append(denominator)
            weight[molecule].append(v)
            graph[denominator].append(molecule)
            weight[denominator].append(1/v)

        result = []
        marked = set()

        def dfs(molecule, denominator, value):
            if molecule in marked: return 0.0
            if molecule not in graph: return 0.0
            if molecule == denominator: return value
            marked.add(molecule)

            temp = 0.0
            for n, w in zip(graph[molecule], weight[molecule]):
                temp = dfs(n, denominator, value*w)
                if temp != 0.0: break

            marked.remove(molecule)
            return temp

        for m, d in queries:
            temp = dfs(m, d, 1.0)
            result.append(temp if temp != 0.0 else -1.0)

        return result


if __name__ == '__main__':
    s = Solution()
    e = [["a", "b"], ["b", "c"]]
    v = [2.0, 3.0]
    q = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    result = s.calcEquation(e, v, q)
    print(result)
