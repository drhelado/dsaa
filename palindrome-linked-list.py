# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        # solution with slow and fast pointer
        # reversing the list from the middle

        s = f = head

        # looping the list with both pointers
        # only checking the fast pointer because it moves first
        while f is not None and f.next is not None:
            s = s.next
            f = f.next.next

        # slow pointer is now in the middle
        # reverse the list from middle
        prev = None
        while s:
            next = s.next
            s.next = prev
            prev = s
            s = next

        # s = reversed(s)

        # check first half and second half of list
        l, r = head, prev
        while r:
            if l.val != r.val:
                return False
            l = l.next
            r = r.next

        return True
