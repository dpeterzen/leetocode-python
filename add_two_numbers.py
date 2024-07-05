# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        while l1 or l2 or carry:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            carry, out = divmod(val1 + val2 + carry, 10)
            
            current.next = ListNode(out)
            current = current.next
            
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
        
        return dummy_head.next
    

        # dummy_head = ListNode()
        # current = dummy_head

        # dummy_next = ListNode(1)
        # next = dummy_next

        # current.next = next
        # # the current node is the dummy_head
        # # the current node has a val of 0 
        # # the current node has a next node of dummy_next
        # # 
        # # the next node is the dummy_next
        # # the next node has a val of 1
        # # the next node has a next node of None