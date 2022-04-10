class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = []
        ans = 0
        for c in s:
            if c == '(':
                if ans:
                    st.append(ans)
                    ans = 0
                st.append(c)
            else: # c == ')'
                if st[-1] == '(':
                    if ans == 0:
                        ans += 1
                    else:
                        ans *= 2
                elif st[-1] == ')':
                    ans *= 2
                elif isinstance(st[-1], int):
                    while isinstance(st[-1], int):
                        ans += st[-1]
                        st.pop()
                    ans *= 2

                st.pop()

        while st and isinstance(st[-1], int):
            ans += st.pop()

        return ans
