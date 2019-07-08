class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        l3 = ListNode(0)
        result = l3
        while l1 and l2:
            sum = l1.val + l2.val +carry
            carry,val = divmod(sum,10)
            l1 = l1.next
            l2 = l2.next
            l3.next = ListNode(val)
            l3 = l3.next
        while l1:
            sum = l1.val + carry
            if sum >= 10:
                l3.next = ListNode(0)
                carry = 1
            if sum<10:
                l3.next = ListNode(sum)
                carry = 0
            l1 = l1.next
            l3 = l3.next
        while l2:
            sum = l2.val + carry
            if sum >= 10:
                l3.next = ListNode(0)
                carry = 1
            if sum < 10:
                l3.next = ListNode(sum)
                carry = 0
            l2 = l2.next
            l3 = l3.next
        else:
            if carry != 0:
                l3.next = ListNode(1)
        return result.next
