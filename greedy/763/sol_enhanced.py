class Solution(object):
    # https://leetcode.com/problems/partition-labels/
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        last_p = {c: i for i, c in enumerate(s)}
        ans = []
        curr_start = curr_last = 0

        for i, c in enumerate(s):
            curr_last = max(curr_last, last_p[c])
            if i == curr_last:
                ans.append(curr_last - curr_start + 1)
                curr_start = i + 1

        return ans

