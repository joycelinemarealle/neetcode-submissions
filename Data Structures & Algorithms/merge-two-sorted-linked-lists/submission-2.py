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

        if list1:
            list3.next = list1
        else:
            list3.next = list2

        return sentinel.next
        #pointer to current end of merge list
        #build merge lists step by step
        #compare and tak smaller head form lst1 or list2
        #if one list mepty attach remianing nodes to merge lists
        #using dummy node makes it handle the head of a merge list

        #create dummy node and add a node pointer
        #while both lists valid have nodes
            #compare list1 val and list2vale
          #add smaller one to mergers
            #move offorware in the chosen list
            #move node to node.next
        #when one list is empty then attach remaing nodes to merge lists
        #return dummy.next which is head of merged list
        