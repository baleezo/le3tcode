class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = [0]
        for c in s:
            if c == '(':
                st.append(0)
            else: # c == ')'
                v = st.pop()
                st[-1] += max(2 * v, 1)

        return st.pop()
