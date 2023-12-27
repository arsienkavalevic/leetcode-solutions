# https://leetcode.com/problems/rotate-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        tail = head
        count = 1
        while tail.next:
            tail = tail.next
            count += 1
        k = k % count

        tail.next = head
        tail = head
        for _ in range(count - k - 1):
            tail = tail.next
        result = tail.next
        tail.next = None

        return result