# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # start both slow and first pointer at root
        s = f = head

        # loop list with both pointers until the fast pointer reaches the end
        # only have to check the fast pointer because it will be the first to move forward
        while f is not None and f.next is not None:
            s = s.next
            f = f.next.next

        return s
