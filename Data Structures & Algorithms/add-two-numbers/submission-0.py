# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


#  5 3 4
#  6 7 2
#  1 1 7
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head = ListNode()

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            sumh = v1 + v2 + carry

            rem = sumh % 10
            carry = sumh // 10
        
            dummy.next = ListNode(rem)
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
            dummy = dummy.next


        return head.next


            
