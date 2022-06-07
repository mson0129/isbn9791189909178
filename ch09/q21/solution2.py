from typing import *
import collections, re

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # 스택을 이용한 문자 제거
        counter, seen, stack = collections.Counter(s), set(), []

        for char in s:
            counter[char] -= 1
            if char in stack:
                continue
            # 뒤에 붙일 문자가 남아 있다면 스택에서 제거
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)
        
        return ''.join(char)