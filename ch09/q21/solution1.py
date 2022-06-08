from typing import *
import collections, re

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # 재귀를 이용한 분리
        for char in sorted(set(s)):
            suffix = s[s.index(char):]
            # 전체 집합과 접미사 집합이 일치할 때 분리 진행
            if set(s) == set(suffix):
                return char + self.removeDuplicateLetters(suffix.replace(char, ''))
        return ''