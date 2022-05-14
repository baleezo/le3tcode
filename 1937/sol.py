class Solution(object):
    # https://leetcode.com/problems/maximum-number-of-points-with-cost/
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        m, n = len(points), len(points[0])
        L = [0] * n
        R = [0] * n
        dp = points[0][:]

        for i in range(1, m):
            L[0] = dp[0]
            R[-1] = dp[n - 1]

            for k in range(1, n):
                L[k] = max(L[k - 1] - 1, dp[k])
                r = n - k - 1
                R[r] = max(dp[r], R[r + 1] - 1)

            for j in range(n):
                dp[j] = points[i][j] + max(L[j], R[j])

        return max(dp)
