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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 재귀 구조로 연결
        if (not list1) or (list2 and list1.val > list2.val):
            list1, list2 = list2, list1 # 스왑
        if list1:
            list1.next = self.mergeTwoLists(list1.next, list2)
        return list1