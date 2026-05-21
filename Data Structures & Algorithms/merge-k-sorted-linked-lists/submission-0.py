# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        for i in range(len(lists)-1,0,-1):
            lists[i-1] = self.mergeTwoLists(lists[i], lists[i-1])
        return lists[0]
        
    def mergeTwoLists(self, list1, list2):
        dummy = node = ListNode()
        l1 = list1
        l2 = list2

        while l1 and l2:
            if l2.val < l1.val:
                node.next = l2
                l2 = l2.next
                node = node.next
            else:
                node.next = l1
                l1 = l1.next
                node = node.next
        if l1:
            node.next = l1
        if l2:
            node.next = l2
        return dummy.next

                