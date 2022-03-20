class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def per(nums, s):
            if s == len(nums) - 1:
                yield [nums[s]]

            curr_h = set()

            for i in range(s, len(nums)):
                if nums[i] in curr_h:
                    continue
                else:
                    curr_h.add(nums[i])

                nums[s], nums[i] = nums[i], nums[s]

                for sub_p in per(nums, s + 1):
                    yield [nums[s]] + sub_p

                nums[s], nums[i] = nums[i], nums[s]

        return per(nums, 0) if nums else nums
