class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0
        dp = [0 for x in range(cols+1)]
        maxsqlen, prev = 0, 0

        for i in range(1, rows+1):
            for j in range(1, cols+1):
                temp = dp[j]
                if matrix[i-1][j-1] == "1":
                    dp[j] = min(dp[j-1], prev, dp[j]) + 1
                    maxsqlen = max(maxsqlen, dp[j])
                else:
                    dp[j] = 0
                prev = temp

        return maxsqlen * maxsqlen


if __name__ == '__main__':
    s = Solution()
    result = s.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])
    print(result)
