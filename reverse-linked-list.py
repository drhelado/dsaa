# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # start pointer from root
        n = head

        prev = None
        while n:
            next = n.next
            n.next = prev
            prev = n
            n = next

            # [1,2,3] -> [(3,1),2,()] -> [3,(1,2),()] -> [3,1,2]
            # [3,4,5] -> [(5,3),4,()] -> [5,(3,4),()] -> [5,3,4]

        return prev
