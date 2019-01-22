#  array dynamic_programming


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        result = 0
        buy = prices[0]
        for x in prices[1:]:
            if x > buy:
                result = max(result, x - buy)
            else:
                buy = x
        return result


if __name__ == '__main__':
    p = [7, 1, 5, 3, 6, 4]
    r = Solution().maxProfit(p)
    assert r == 5, r

    p = [4, 6, 1, 2]
    r = Solution().maxProfit(p)
    assert r == 2, r

    p = [7, 6, 4, 3, 1]
    r = Solution().maxProfit(p)
    assert r == 0, r

    p = []
    r = Solution().maxProfit(p)
    assert r == 0, r

    p = [42]
    r = Solution().maxProfit(p)
    assert r == 0, r
