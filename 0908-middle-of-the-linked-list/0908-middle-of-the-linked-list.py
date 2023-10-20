# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        count = 0
        while temp:
            temp = temp.next
            count += 1

        if count % 2 == 0:
            mid = int(count / 2)
        else:
            mid = int(count // 2)
        
        curr = head
        for i in range(mid):
            curr = curr.next
        return curr


        