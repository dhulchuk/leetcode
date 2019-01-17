#  array math


class Solution:
    def sumSubseqWidths(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        return sum(
            x * ((1 << i) - (1 << len(A) - i - 1))
            for i, x in enumerate(A)
        ) % (10 ** 9 + 7)


if __name__ == '__main__':
    r = Solution().sumSubseqWidths([1, 2])
    assert r == 1, r
    r = Solution().sumSubseqWidths([1, 2, 3])
    assert r == 6, r
    r = Solution().sumSubseqWidths([9, 1, 25, 29, 21, 30, 37, 2, 39, 6, 28, 16, 32, 32, 7, 3, 15, 39, 32, 11])
    assert r == 37210632, r
    r = Solution().sumSubseqWidths(
        [5, 69, 89, 92, 31, 16, 25, 45, 63, 40, 16, 56, 24, 40, 75, 82, 40, 12, 50, 62, 92, 44, 67, 38, 92, 22, 91, 24,
         26, 21, 100, 42, 23, 56, 64, 43, 95, 76, 84, 79, 89, 4, 16, 94, 16, 77, 92, 9, 30, 13])
    assert r == 857876214, r
