class Solution(object):
    # https://leetcode.com/problems/valid-palindrome-ii/
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l, r = 0, len(s) - 1
        def varify(l , r):
            while l < r:
                if s[l] == s[r]:
                    r -= 1
                    l += 1
                else:
                    return False

            return True

        while l < r:
            if s[l] != s[r]:
                return varify(l + 1, r) or varify(l, r - 1)

            l += 1
            r -= 1

        return True
