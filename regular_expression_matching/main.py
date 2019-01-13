class Solution:
    def __init__(self):
        self.s = None
        self.p = None
        self.cache = {}

    def match_indexes(self, s_ind, p_ind):
        if (s_ind, p_ind) in self.cache:
            return self.cache[(s_ind, p_ind)]
        while True:
            if p_ind >= len(self.p):
                return s_ind >= len(self.s)
            if p_ind == len(self.p) - 1 or self.p[p_ind + 1] != '*':  # exactly same character
                if s_ind < len(self.s) and (self.p[p_ind] == '.' or self.p[p_ind] == self.s[s_ind]):
                    s_ind += 1
                else:
                    self.cache[(s_ind, p_ind)] = False
                    return False
            else:  # variations with '?*'
                save = s_ind
                while s_ind < len(self.s) and (self.p[p_ind] == '.' or self.p[p_ind] == self.s[s_ind]):
                    if self.match_indexes(s_ind + 1, p_ind + 2):  # how much * can use
                        self.cache[(s_ind, p_ind)] = True
                        return True
                    s_ind += 1
                res = self.match_indexes(save, p_ind + 2)  # * do nothing
                self.cache[(s_ind, p_ind)] = res
                return res
            p_ind += 1

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        self.s, self.p = s, p
        return self.match_indexes(0, 0)


class Solution2:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s_ind = p_ind = 0
        while True:
            if p_ind >= len(p):
                return s_ind >= len(s)
            if p_ind == len(p) - 1 or p[p_ind + 1] != '*':  # exactly same character
                if s_ind < len(s) and (p[p_ind] == '.' or p[p_ind] == s[s_ind]):
                    s_ind += 1
                else:
                    return False
            else:  # variations with '?*'
                save = s_ind
                while s_ind < len(s) and (p[p_ind] == '.' or p[p_ind] == s[s_ind]):
                    if self.isMatch(s[s_ind + 1:], p[p_ind + 2:]):  # how much * can use
                        return True
                    s_ind += 1
                return self.isMatch(s[save:], p[p_ind + 2:])  # * do nothing
            p_ind += 1


class Solution3:
    def isMatch(self, s, p):
        if not p:
            return not bool(s)
        if not s:
            return len(p) % 2 == 0 and set(p[1::2]) == {'*'}
        match = p[0] == '.' or p[0] == s[0]
        if len(p) == 1 or p[1] != '*':  # exactly same character
            return match and self.isMatch(s[1:], p[1:])
        return (match and self.isMatch(s[1:], p)) or self.isMatch(s, p[2:])


if __name__ == '__main__':
    Solution = Solution3
    assert Solution().isMatch("a", "a*a") is True
    assert Solution().isMatch("abc", "abc") is True
    assert Solution().isMatch("aa", "a") is False
    assert Solution().isMatch("", "") is True
    assert Solution().isMatch("q", "qw") is False
    assert Solution().isMatch("aa", "a*") is True
    assert Solution().isMatch("ab", ".*") is True
    assert Solution().isMatch("aab", "c*a*b*") is True
    assert Solution().isMatch("mississippi", "mis*is*p*.") is False
    # #
    assert Solution().isMatch("qqqq", "q*qw*") is True
    assert Solution().isMatch("qqqq", "q*qw*e") is False
    # #
    assert Solution().isMatch("aaa", "ab*a*c*a") is True
    # #
    assert Solution().isMatch("bbbba", ".*a*a") is True
    assert Solution().isMatch("a", ".*a.*") is True
    assert Solution().isMatch("ab", ".*..c*") is True
