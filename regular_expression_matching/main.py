class Solution:
    def isMatch(self, s, p):
        cache = {}

        def match_indexes(s_ind, p_ind):
            if (s_ind, p_ind) not in cache:
                if p_ind == len(p):
                    res = s_ind == len(s)
                else:
                    match = s_ind < len(s) and p[p_ind] in ('.', s[s_ind])
                    if p_ind == len(p) - 1 or p[p_ind + 1] != '*':
                        res = match and match_indexes(s_ind + 1, p_ind + 1)
                    else:
                        res = match and match_indexes(s_ind + 1, p_ind) or match_indexes(s_ind, p_ind + 2)
                cache[s_ind, p_ind] = res
            return cache[(s_ind, p_ind)]

        return match_indexes(0, 0)


if __name__ == '__main__':
    assert Solution().isMatch("a", "a*a") is True
    assert Solution().isMatch("abc", "abc") is True
    assert Solution().isMatch("aa", "a") is False
    assert Solution().isMatch("", "") is True
    assert Solution().isMatch("q", "qw") is False
    assert Solution().isMatch("aa", "a*") is True
    assert Solution().isMatch("ab", ".*") is True
    assert Solution().isMatch("aab", "c*a*b*") is True
    assert Solution().isMatch("mississippi", "mis*is*p*.") is False
    #
    assert Solution().isMatch("qqqq", "q*qw*") is True
    assert Solution().isMatch("qqqq", "q*qw*e") is False
    #
    assert Solution().isMatch("aaa", "ab*a*c*a") is True
    #
    assert Solution().isMatch("bbbba", ".*a*a") is True
    assert Solution().isMatch("a", ".*a.*") is True
    assert Solution().isMatch("ab", ".*..c*") is True
