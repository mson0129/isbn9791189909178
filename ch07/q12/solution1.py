from typing import *
import collections, re, sys

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 브루트 포스로 계산
        max_price = 0

        for i, price in enumerate(prices):
            for j in range(i, len(prices)):
                max_price = max(prices[j] - price, max_price)
        
        return max_price