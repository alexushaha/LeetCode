# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry=0
        returnHead=ListNode(0)
        returnCur=returnHead
        while l1 or l2 or carry:
            sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry = sum // 10
            digit = sum % 10
            returnCur.next = ListNode(digit)
            returnCur = returnCur.next
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        return returnHead.next