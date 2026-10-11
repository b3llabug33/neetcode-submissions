# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        cur = head
        slow = cur
        fast = cur
        while fast and fast.next:
             slow = slow.next
             fast = fast.next.next
        second = slow.next
        slow.next = None
     
        back = None
        while second:
             saveTemp = second.next
             second.next = back
             back = second
             second = saveTemp
        reversedSecond = back

        first = head
        second = reversedSecond 

        while second:
             tmp1 = first.next 
             tmp2 = second.next
             first.next = second
             second.next = tmp1
             first = tmp1
             second = tmp2

             
        

            

             
        