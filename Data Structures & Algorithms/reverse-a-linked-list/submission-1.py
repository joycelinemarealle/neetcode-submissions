# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
         #loops through nodes as node not empty flip curr.next = prev , curret = prev, 
        prev,curr = None, head
        while curr:
            #save next
            nxt = curr.next
            #assign new next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
            
        