# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        temp_sum = 0

        while l1 or l2 or temp_sum:
            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0
            temp_sum += digit1 + digit2
            node = ListNode(temp_sum % 10)
            temp_sum //= 10
            tail.next = node
            tail = tail.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next