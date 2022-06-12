# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # reset variable names
        l1, l2 = list1, list2

        dummy = ListNode()

        # start looping list from dummy
        n = dummy

        # loop the max length of both lists
        while l1 and l2:
            if l1.val < l2.val:
                n.next = l1
                l1 = l1.next
            else:
                n.next = l2
                l2 = l2.next

            # move current node pointer
            n = n.next

        # append to the end the remainder of the longest list
        if l1:
            n.next = l1
        if l2:
            n.next = l2

        # return list starting from root
        return dummy.next
