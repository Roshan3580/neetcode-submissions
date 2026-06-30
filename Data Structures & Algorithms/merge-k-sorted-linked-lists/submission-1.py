# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        def mergeList(l1, l2):
            dummy = node = ListNode()
            while l1 and l2:
                if l1.val <= l2.val:
                    node.next = l1
                    l1 = l1.next
                else:
                    node.next = l2
                    l2 = l2.next
                node = node.next
            if l1:
                node.next = l1
            if l2:
                node.next = l2
            return dummy.next
        
        for i in range(len(lists) - 1, 0, -1):
            lists[i-1] = mergeList(lists[i], lists[i-1])
        return lists[0]
            