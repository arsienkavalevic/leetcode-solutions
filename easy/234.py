# https://leetcode.com/problems/palindrome-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        fast = None
        while slow:
            temp = slow.next
            slow.next = fast
            fast = slow
            slow = temp

        while fast and head:
            if fast.val != head.val:
                return False
            fast = fast.next
            head = head.next
        return True