from typing import *
import collections, re

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 반복 구조로 뒤집기 - solution1에 비해 공간 복잡도가 좀 더 낮음
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        
        return prev