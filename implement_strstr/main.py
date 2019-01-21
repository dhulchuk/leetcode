#  two_pointers string
#  TODO: KMP or Boyer-Moore


class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        i = j = 0
        while True:
            if j == len(needle):
                return i
            if i > len(haystack) - len(needle):
                return -1
            if haystack[i + j] == needle[j]:
                j += 1
            else:
                j = 0
                i += 1


if __name__ == '__main__':
    haystack = 'hello'
    needle = 'll'
    res = Solution().strStr(haystack, needle)
    assert res == 2, res

    haystack = 'hello'
    needle = 'qwe'
    res = Solution().strStr(haystack, needle)
    assert res == -1, res

    haystack = 'hello'
    needle = ''
    res = Solution().strStr(haystack, needle)
    assert res == 0, res

    haystack = 'helloll'
    needle = 'll'
    res = Solution().strStr(haystack, needle)
    assert res == 2, res

    haystack = 'qqqe'
    needle = 'qqe'
    res = Solution().strStr(haystack, needle)
    assert res == 1, res

    haystack = 'aaa'
    needle = 'aaaa'
    res = Solution().strStr(haystack, needle)
    assert res == -1, res
