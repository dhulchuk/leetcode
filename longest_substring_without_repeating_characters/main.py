class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = [0] * 128
        res = 0
        sample_start = 0
        for i, x in enumerate(s):
            i = i + 1
            x_ch = ord(x)
            prev_x_index = d[x_ch]
            sample_start = max(prev_x_index, sample_start)
            res = max(res, i - sample_start)
            d[x_ch] = i
        return res


if __name__ == '__main__':
    r1 = Solution().lengthOfLongestSubstring("abcabcbb")
    assert r1 == 3, r1

    r2 = Solution().lengthOfLongestSubstring("bbbbb")
    assert r2 == 1, r2

    r3 = Solution().lengthOfLongestSubstring("pwwkew")
    assert r3 == 3, r3

    r4 = Solution().lengthOfLongestSubstring(" ")
    assert r4 == 1, r4

    r5 = Solution().lengthOfLongestSubstring("azzqweza")
    assert r5 == 5, r5

    r6 = Solution().lengthOfLongestSubstring("cdd")
    assert r6 == 2, r6

    r7 = Solution().lengthOfLongestSubstring("ohomm")
    assert r7 == 3, r7
