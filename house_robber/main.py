#  dynamic_programming


class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cache = [-1] * len(nums)

        def by_index(i):
            if i == -1:
                return 0
            elif i == 0:
                res = nums[0]
            elif cache[i] >= 0:
                return cache[i]
            elif i == 1:
                res = max(nums[0], nums[1])
            else:
                res = max(nums[i] + by_index(i - 2),
                          nums[i - 1] + by_index(i - 3))
            cache[i] = res
            return res

        return by_index(len(nums) - 1)


if __name__ == '__main__':
    in1 = [1, 2, 3, 1]
    assert Solution().rob(in1) == 4

    in2 = [2, 7, 9, 3, 1]
    assert Solution().rob(in2) == 12

    in3 = [2, 1, 1, 3, 1]
    assert Solution().rob(in3) == 5

    in4 = [226, 174, 214, 16, 218, 48, 153, 131, 128, 17, 157, 142, 88, 43, 37, 157, 43, 221, 191, 68, 206, 23, 225, 82,
           54, 118, 111, 46, 80, 49, 245, 63, 25, 194, 72, 80, 143, 55, 209, 18, 55, 122, 65, 66, 177, 101, 63, 201,
           172, 130, 103, 225, 142, 46, 86, 185, 62, 138, 212, 192, 125, 77, 223, 188, 99, 228, 90, 25, 193, 211, 84,
           239, 119, 234, 85, 83, 123, 120, 131, 203, 219, 10, 82, 35, 120, 180, 249, 106, 37, 169, 225, 54, 103, 55,
           166, 124]
    assert Solution().rob(in4) == 7102, Solution().rob(in4)

    in5 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert Solution().rob(in5) == 0, Solution().rob(in5)
