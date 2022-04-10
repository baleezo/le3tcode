class Solution(object):
    # https://leetcode.com/problems/broken-calculator/
    # if target is even, it from sth * 2
    # if target if odd, it from sth * 2 - 1 (minimal step)
    # greedy
    def brokenCalc(self, startValue, target):
        """
        :type startValue: int
        :type target: int
        :rtype: int
        """
        if startValue >= target:
            return abs(target - startValue)

        step = 0
        while target != startValue:
            if target < startValue:
                step += startValue - target
                break
            elif target % 2 != 0:
                target += 1
                step += 1
            else:
                target /= 2
                step += 1

        return step
