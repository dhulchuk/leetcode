#  backtracking


class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        used = set()
        return [nums] if len(nums) == 1 else [
            [x] + mut
            for i, x in enumerate(nums)
            if x not in used and (used.add(x) or True)
            for mut in self.permuteUnique(nums[:i] + nums[i + 1:])
        ]


if __name__ == '__main__':
    input = [1, 1]
    output = [
        [1, 1],
    ]
    assert Solution().permuteUnique(input) == output, Solution().permuteUnique(input)

    input = [1, 1, 2]
    output = [
        [1, 1, 2],
        [1, 2, 1],
        [2, 1, 1]
    ]
    assert Solution().permuteUnique(input) == output, Solution().permuteUnique(input)

    input = [1]
    output = [[1]]
    assert Solution().permuteUnique(input) == output

    input = [1, 2]
    output = [[1, 2], [2, 1]]
    assert Solution().permuteUnique(input) == output

    input = []
    output = []
    assert Solution().permuteUnique(input) == output
