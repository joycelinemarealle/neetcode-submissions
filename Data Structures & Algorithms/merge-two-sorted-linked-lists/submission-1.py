# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode()
        list3 = sentinel

        while list1 and list2:
            if list1.val < list2.val:
                list3.next = ListNode(list1.val)
                list1 = list1.next
            else:
                list3.next = ListNode(list2.val)
                list2 = list2.next
            list3 = list3.next
        #if any list has remaining nodes just attach
        if list1:
            list3.next = list1
        else:
            list3.next = list2
            
        return sentinel.next      

        #create a dummy node
        #while both lists exist
        #compare the list1.val and list2.val
            #attach smallar node to node.next
            #move forward chosen lis
        #when one list is empty i want attach remaining notes
        #return dummy.next which is head of merged list