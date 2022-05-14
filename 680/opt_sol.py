class Solution(object):
    # https://leetcode.com/problems/valid-palindrome-ii/
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        def verify(l , r, skip=False):
            while l < r:
                if s[l] == s[r]:
                    r -= 1
                    l += 1
                else:
                    if skip:
                        return False

                    return verify(l + 1, r, skip=True) or verify(l, r - 1, skip=True)

            return True

        return verify(0, len(s) - 1)
