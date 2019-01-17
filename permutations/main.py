#  backtracking


class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1:
            return [nums]
        res = []
        for i, x in enumerate(nums):
            submuts = self.permute(nums[:i] + nums[i + 1:])
            for mut in submuts:
                res.append([x] + mut)
        return res


if __name__ == '__main__':
    input = [1, 2, 3]
    output = [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1]
    ]
    assert Solution().permute(input) == output

    input = [1]
    output = [[1]]
    assert Solution().permute(input) == output

    input = [1, 2]
    output = [[1, 2], [2, 1]]
    assert Solution().permute(input) == output

    input = []
    output = []
    assert Solution().permute(input) == output
