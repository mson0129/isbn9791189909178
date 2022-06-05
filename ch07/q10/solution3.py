from typing import *
import collections, re

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # 파이썬 다운 방식
        return sum(sorted(nums)[::2])