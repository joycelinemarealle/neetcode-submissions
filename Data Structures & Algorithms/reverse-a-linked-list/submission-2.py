# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev,curr = None, head

        #not null
        while curr:
            #store next pointer
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

        #intialize prev as null, curr as head
        #check that cur not null
        #while curr exists
        #save the next pointer curr.next
        #curr.next = prev, prev =curr
        #then update curr = next
        #return prev
        
        