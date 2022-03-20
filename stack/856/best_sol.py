class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = bal = 0
        for i, c in enumerate(s):
            if c == '(':
                bal += 1
            else: # c == ')'
                bal -= 1
                if s[i - 1] == '(': # found core -> 1
                    ans += 1 << bal # 2 to the power of bal (exterior set of parentheses)

        return ans

