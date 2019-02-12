#  array divide_and_conquer dynamic_programming
from typing import List


class Solution:
    def maxSubArray(self, nums: 'List[int]') -> 'int':
        mini, res = 0, nums[0]
        summ, maxi = 0, 0
        for x in nums:
            mini = min(mini, summ)
            summ += x
            res = max(res, summ - mini)
        return res


if __name__ == '__main__':
    assert Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    r = Solution().maxSubArray([-1, -1, -1])
    assert r == -1, r
