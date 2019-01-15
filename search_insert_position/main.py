#  array binary_search


class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo, hi = 0, len(nums)
        while True:
            if lo == hi - 1:
                return lo if nums[lo] >= target else hi
            p = (lo + hi) // 2
            if target > nums[p]:
                lo = p
            else:
                hi = p


if __name__ == '__main__':
    assert Solution().searchInsert([1, 3, 5, 6], 5) == 2
    assert Solution().searchInsert([1, 3, 5, 6], 2) == 1
    assert Solution().searchInsert([1, 3, 5, 6], 7) == 4
    assert Solution().searchInsert([1, 3, 5, 6], 0) == 0
    assert Solution().searchInsert([1, 3, 5, 7, 8], 6) == 3
    assert Solution().searchInsert([1, 3, 5, 7, 8], 4) == 2
    assert Solution().searchInsert([1, 3, 5, 7, 8], 0) == 0
