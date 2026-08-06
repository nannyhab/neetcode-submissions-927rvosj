# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fastPtr = head
        slowPtr = head

        while fastPtr != None and fastPtr.next != None:
            fastPtr = fastPtr.next.next
            slowPtr = slowPtr.next

            if fastPtr == slowPtr:
                return True
        return False