class Solution(object):
    # https://leetcode.com/problems/maximum-number-of-points-with-cost/
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        def dp(i, j):
            if i == 0:
                return points[i][j]
            if res[i][j] is None:
                res[i][j] = max([dp(i - 1, k) + points[i][j] - abs(k- j) for k in range(n)])

            return res[i][j]


        m, n = len(points), len(points[0])
        res = [[None] * n for _ in  range(m)]

        ans = max([dp(m - 1, k) for k in range(n)])
        return ans
