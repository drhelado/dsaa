# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # start with a pointer from root
        n = head

        # loop list
        while n:
            # remove duplicates
            while n.next and n.val == n.next.val:
                n.next = n.next.next

            n = n.next

        return head
