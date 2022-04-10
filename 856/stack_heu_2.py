class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = []
        for c in s:
            if c == '(':
                st.append(c)
            else: # c == ')'
                v = st.pop()
                if v == '(':
                    v = 1 # ()
                else:
                    v = 2 * v
                    st.pop() # remove the corresponding (

                if not st or st[-1] == '(':
                    st.append(v)
                else: # if the top of stack is a score, add the current score to it
                    st[-1] += v

        return st.pop()
