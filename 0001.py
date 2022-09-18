# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        re = p = ListNode(0)
        carry = 0

        while l1 or l2 or carry:

            carry += (l1.val if l1 else None) + (l2.val if l2 else None)# 値を計算

            p.next = carry % 10
            carry = carry // 10# update carry

            l1 = l1.next if l1 else None
            l2 = l2.next if l1 else None

            p = p.next





if __name__ == '__main__':
    pass
