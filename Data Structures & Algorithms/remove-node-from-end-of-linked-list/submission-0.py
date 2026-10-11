# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        num = 0
        cur = head
        while cur:
             num += 1
             cur = cur.next
        nodeToRemove = num - n
        count = 0
        dummy = ListNode(0, head)
        cur2 = dummy
        while cur2:
             if count == nodeToRemove:
                 cur2.next = cur2.next.next
             count += 1
             cur2 = cur2.next
        return dummy.next
             
        
             
        