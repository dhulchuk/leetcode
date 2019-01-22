#  array greedy


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return sum(
            prices[i] - prices[i - 1]
            for i in range(1, len(prices))
            if prices[i] > prices[i - 1]
        )


if __name__ == '__main__':
    p = [7, 1, 5, 3, 6, 4]
    r = Solution().maxProfit(p)
    assert r == 7, r

    p = [1, 2, 3, 4, 5]
    r = Solution().maxProfit(p)
    assert r == 4, r

    p = [7, 6, 4, 3, 1]
    r = Solution().maxProfit(p)
    assert r == 0, r

    p = [1, 2, 3, 4, 5, 42, 1]
    r = Solution().maxProfit(p)
    assert r == 41, r

    p = [7]
    r = Solution().maxProfit(p)
    assert r == 0, r

    p = []
    r = Solution().maxProfit(p)
    assert r == 0, r
