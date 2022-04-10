class Solution(object):
    # DP
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        ans = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if j - 1 < 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i][j - 1 ] + 1
                else:
                    continue

                curr_w = n

                for h in range(i + 1):
                    curr_w = min(curr_w, dp[i - h][j])

                    if curr_w == 0:
                        break

                    ans = max(ans, (h + 1) * curr_w)

        return ans

