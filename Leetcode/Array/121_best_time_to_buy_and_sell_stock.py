import sys
from typing import List

def maxProfit(prices: List[int]) -> int:
    profit = 0
    min_price = sys.maxsize

    #최솟값과 최대차이를 갱신
    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)

    return profit

print(maxProfit([7,1,5,3,6,4]))