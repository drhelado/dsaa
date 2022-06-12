# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        # set node before the root of list
        dummy = ListNode(next = head)

        # prev and curr pointers
        p, c = dummy, head

        # loop list starting from head
        while c:
            # remove element by skipping it if it's the value we want to remove
            if c.val == val:
                p.next = c.next
            else:
                p = c

            c = c.next

        # return the new list without including dummy node
        return dummy.next
