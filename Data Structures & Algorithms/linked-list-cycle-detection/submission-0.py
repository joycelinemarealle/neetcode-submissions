# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True #has a cycle
        return False #no cycle
        #slow and fast pointer
        #if there is a cycle then slow and fast will meet
        #if not then fast will reach null and loop stops

        #initlaize pointers
        #move htrough list slow, fast
            #if slow = fast then tre
        #if fast reached null no cycle exis return fasle
        #time O(n) , space O(1) because using pointers        