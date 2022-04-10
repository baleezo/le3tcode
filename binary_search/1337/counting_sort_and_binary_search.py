class Solution(object):
    # https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
    # 1. counting sort
    # 2. binary_search for counting each row -> O(n) -> O(lgn) for each row -> O(mlgn) for total
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """

        res = [[] for _ in range(len(mat[0]) + 1)]

        for i, row in enumerate(mat):
            l = 0
            h = len(row)
            while l <  h:
                m = (l + h) // 2
                if row[m]:
                    l = m + 1
                else:
                    h = m

            res[l].append(i)

        ans = []
        for r in res:
            for a in r:
                ans.append(a)
                if len(ans) == k:
                    return ans

