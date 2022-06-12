# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # print(l1)
        # exit()

        head = None
        prev = None
        temp = None
        carry = 0

        while (l1 is not None or l2 is not None):

            l1Data = 0 if l1 is None else l1.val
            l2Data = 0 if l2 is None else l2.val
            Sum = carry + l1Data + l2Data

            carry = 1 if Sum >= 10 else 0

            Sum = Sum if Sum < 10 else Sum % 10

            temp = ListNode(Sum)

            if head is None:
                head = temp
            else:
                prev.next = temp

            # Set current node as new prev
            prev = temp

            if l1 is not None:
                l1 = l1.next

            if l2 is not None:
                l2 = l2.next

        # print(head)
        # exit()

        # If last addition has carry, add new node with the carry
        if carry > 0:
            temp.next = ListNode(carry)


        # return
        return head
