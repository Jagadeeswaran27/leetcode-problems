# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k==0:
            return head
        if not head:
            return None
        temp = head
        count = 1
        while temp.next:
            count += 1
            temp = temp.next
        temp.next = head
        k = k%count
        for i in range(count-k):
            temp = temp.next
        
        newHead = temp.next
        temp.next = None

        return newHead