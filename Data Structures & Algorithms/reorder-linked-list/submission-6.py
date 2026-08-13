# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head

        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next

        curr = slow.next
        slow.next = None
        prev = None
        while curr != None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        first = head
        second = prev
        while second != None:
            print(f"this is first {first.val} and second {second.val}")
            tmpNext1 = first.next
            tmpNext2 = second.next

            first.next = second
            second.next = tmpNext1

            first = tmpNext1
            second = tmpNext2

        
            

