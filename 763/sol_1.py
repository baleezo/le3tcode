class Solution(object):
    # https://leetcode.com/problems/partition-labels/
    # greedy
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        segs = []
        c_map = {}
        for i, c in enumerate(s):
            if c not in c_map:
                segs.append([i, i])
                c_map[c] = len(segs) - 1
            else:
                segs[c_map[c]][1] = i

        ans = []
        seg_c = segs[0]
        for seg in segs[1:]:
            if seg_c[1] < seg[0]:
                ans.append(seg_c[1] - seg_c[0] + 1)
                seg_c = seg
            else:
                seg_c[0], seg_c[1] = min(seg_c[0], seg[0]), max(seg_c[1], seg[1])

        ans.append(seg_c[1] - seg_c[0] + 1)

        return ans
