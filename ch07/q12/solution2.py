from typing import *
import collections, re, sys

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 저점과 현재 값과의 차이 계산
        profit = 0
        min_price = sys.maxsize

        # 최소값과 최댓값을 계속 갱신
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
        
        return profit