class Solution(object):
    # https://leetcode.com/problems/minimum-size-subarray-sum/solution/
    # sliding window / two pointer
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        c_sum = 0
        left = 0
        ans = len(nums) + 1

        for i in range(len(nums)):
            c_sum += nums[i]

            while c_sum >= target:
                ans = min(ans, i - left + 1)
                c_sum -= nums[left]
                left += 1

        if ans <= len(nums):
            return ans

        return 0
