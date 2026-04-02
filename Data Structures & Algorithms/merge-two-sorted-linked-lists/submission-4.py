# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = list1
        ptr2 = list2

        dummy = ListNode(0)
        newList = dummy

        while ptr1 and ptr2:
            if ptr1.val >= ptr2.val:
                newList.next = ptr2
                ptr2 = ptr2.next
            else:
                newList.next = ptr1
                ptr1 = ptr1.next
            newList = newList.next

        if ptr1 != None:
            newList.next = ptr1
        if ptr2 != None:
            newList.next = ptr2
        
        return dummy.next
        