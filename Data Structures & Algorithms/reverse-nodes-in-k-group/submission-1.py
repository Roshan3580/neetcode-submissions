# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prevGroup = dummy

        while True:
            kth = self.getK(prevGroup, k)
            if not kth:
                break
            nextGroup = kth.next
            prev, curr = kth.next, prevGroup.next
            while curr != nextGroup:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            temp = prevGroup.next
            prevGroup.next = kth
            prevGroup = temp

        return dummy.next


    def getK(self, curr, k):
        while curr and k:
            curr = curr.next
            k -= 1
        return curr
    