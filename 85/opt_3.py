class Solution(object):
    # DP
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        m, n = len(matrix), len(matrix[0])
        dp = [0] * n
        ans = 0

        for i in range(m):
            stack = []
            for j in range(n):
                if matrix[i][j] == '1':
                    if i - 1 < 0:
                        dp[j] = 1
                    else:
                        dp[j] = dp[j] + 1
                else:
                    dp[j] = 0

                while len(stack) > 0 and dp[stack[-1]] >= dp[j]:
                    height = dp[stack.pop()]

                    if len(stack) == 0:
                        width = j
                    else:
                        width = j - stack[-1] - 1

                    ans = max(ans, width * height)

                stack.append(j)

            f = stack[-1]
            while len(stack) > 0:
                height = dp[stack.pop()]

                if len(stack) == 0:
                    width = f + 1
                else:
                    width = f - stack[-1]

                ans = max(ans, width * height)

        return ans

