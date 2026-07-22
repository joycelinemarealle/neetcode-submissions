# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head #current first node
       
        while curr:  #current not null
            nxt = curr.next #save it before breaking link. temp variable
            #reverse pointers
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

        #two pointers prev, curr
        #while curr is not null revers epointer
        #curr shifts to prev
        #curr to next but save it before you break link
        #return prev since no head
        #big O(n) time big O(1)

        