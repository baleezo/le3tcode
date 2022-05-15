class Solution(object):
    # https://leetcode.com/problems/remove-duplicate-letters/
    # stack
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """

        last_index_of_c = {c: i for i, c in enumerate(s)}
        seen = set()
        st = []

        for i, c in enumerate(s):
            if c not in seen:
                while st and c < st[-1] and i < last_index_of_c[st[-1]]:
                    r = st.pop()
                    seen.remove(r)

                seen.add(c)
                st.append(c)

        return ''.join(st)
