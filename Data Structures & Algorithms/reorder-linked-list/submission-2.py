# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        curr = slow.next
        prev = slow.next = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        l1, l2 = head, prev

        dummy = node = ListNode()
        while l2:
            temp1, temp2 = l1.next, l2.next
            node.next = l1
            node = node.next
            node.next = l2
            node = node.next
            l1, l2 = temp1, temp2
        if l1:
            node.next = l1


