# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fastPtr = head
        slowPtr = head

        while fastPtr and fastPtr.next:
            fastPtr = fastPtr.next.next
            slowPtr = slowPtr.next
        
        middle = slowPtr
        prev = None
        while middle:
            nxt = middle.next
            middle.next = prev
            prev = middle
            middle = nxt

        first = head
        second = prev
        while second.next:  # stop when second half is exhausted
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2
        

        



        