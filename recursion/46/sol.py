class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if len(nums) == 1:
            yield nums

        for _ in range(len(nums)):
            num = nums.pop(0)

            for per in self.permute(nums):
                yield [num] + per

            nums.append(num)
