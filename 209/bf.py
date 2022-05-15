class Solution(object):
    # https://leetcode.com/problems/minimum-size-subarray-sum/solution/
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        p_sum = [0] * len(nums)
        p_sum[0] = nums[0]
        for i in range(1, len(nums)):
            p_sum[i] = nums[i] + p_sum[i - 1]

        ans = len(nums) + 1
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if p_sum[j] - p_sum[i] + nums[i] >= target:
                    ans = min(ans, j - i + 1)
                    break

        if ans <= len(nums):
            return ans

        return 0

