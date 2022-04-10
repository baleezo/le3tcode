class Solution(object):
    # https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
    # by counting sort
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """

        res = [[] for _ in range(len(mat[0]) + 1)]

        for i, row in enumerate(mat):
            res[sum(row)].append(i)

        ans = []

        for r in res:
            for a in r:
                ans.append(a)
                if len(ans) == k:
                    return ans
