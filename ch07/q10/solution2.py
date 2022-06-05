from typing import *
import collections, re

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # 짝수 번째 값 계산
        sum = 0
        nums.sort()

        for i, n in enumerate(nums):
            # 짝수 번째 값의 합 계산
            if i % 2 == 0:
                sum += n
        
        return sum