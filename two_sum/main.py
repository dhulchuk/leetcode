class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        save = dict()
        for i, value in enumerate(nums):
            try:
                j = save[value]
            except KeyError:
                save[target - value] = i
            else:
                return [j, i]


if __name__ == '__main__':
    assert Solution().twoSum([2, 1, 7, 11, 15], 9) == [0, 2]
