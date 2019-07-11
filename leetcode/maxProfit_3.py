class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        first_buy, first_sell, second_buy, second_sell = -sys.maxsize, 0, -sys.maxsize, 0
        for price in prices:
            first_buy = max(first_buy, -price)  # 第一次买入手上的钱
            first_sell = max(first_sell, price+first_buy)  # 第一次卖出手上的钱
            second_buy = max(second_buy, first_sell-price)  # 第二次买入手上的钱
            second_sell = max(second_sell, price+second_buy)  # 第二次卖出手上的钱
        return second_sell
