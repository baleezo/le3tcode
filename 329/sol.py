class Solution(object):
    # https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
    # DFS, DP
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        def dfs(i, j):

            if rec[i][j] is None:
                u = 0
                if i > 0 and matrix[i - 1][j] > matrix[i][j]:
                    u = dfs(i - 1, j)

                r = 0
                if j < n - 1 and matrix[i][j + 1] > matrix[i][j]:
                    r = dfs(i, j + 1)

                d = 0
                if i < m - 1 and matrix[i + 1][j] > matrix[i][j]:
                    d = dfs(i + 1, j)

                l = 0
                if j > 0 and matrix[i][j - 1] > matrix[i][j]:
                    l = dfs(i, j - 1)

                rec[i][j] = max(u, r, d, l) + 1

            return rec[i][j]

        m, n = len(matrix), len(matrix[0])
        rec = [[None] * n for _ in range(m)]
        ans = 0

        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j))

        return ans
