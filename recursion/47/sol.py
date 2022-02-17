class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1:
            yield nums

        nums= sorted(nums)
        prev = None

        for _ in range(len(nums)):
            p = nums.pop(0)

            if p == prev:
                nums.append(p)
                continue
            else:
                prev = p

            for per in self.permuteUnique(nums):
                yield [p] + per

            nums.append(p)
