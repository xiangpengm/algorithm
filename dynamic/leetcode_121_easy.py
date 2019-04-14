"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计
一个算法来计算你所能获取的最大利润。
注意你不能在买入股票前卖出股票。

示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。

示例 2:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max_profit[i] = max(price[i] - min_buy_price[i-1], max_profit[i-1])
        # min_buy_price[i] = min(price[i], min_buy_price[i-1])
        max_profit = 0 
        min_buy_price = prices[0]
        if len(prices) < 2:
            return 0
        for price in prices:
            if price > min_buy_price:
                max_profit = max(price-min_buy_price, max_profit)
            else:
                min_buy_price = min(min_buy_price, price)
        return max_profit



def main():
    s = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    print(s.maxProfit(prices))


if __name__ == "__main__":
    main()
