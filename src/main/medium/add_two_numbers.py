# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example-
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = ListNode(val)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        return self.head

    def print_list(self):
        if self.head is None:
            print("Empty list")
            return
        current = self.head
        while current:
            print(current.val)
            current = current.next


class Solution:
    def add_two_numbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3_list = LinkedList()
        carry = 0
        temp = 0
        temp1 = l1
        temp2 = l2
        while temp1 and temp2:
            temp = temp1.val + temp2.val + carry
            if temp < 10:
                l3_list.append(temp)
                carry = 0
            else:
                l3_list.append(temp%10)
                carry = 1
            temp1 = temp1.next
            temp2 = temp2.next
        if temp1:
            while temp1:
                temp = temp1.val + carry
                if temp < 10:
                    l3_list.append(temp)
                    carry = 0
                else:
                    l3_list.append(temp % 10)
                    carry = 1
                temp1 = temp1.next
        else:
            while temp2:
                temp = temp2.val + carry
                if temp < 10:
                    l3_list.append(temp)
                    carry = 0
                else:
                    l3_list.append(temp % 10)
                    carry = 1
                temp2 = temp2.next
        if carry != 0:
            l3_list.append(carry)
        l3_list.print_list()
        return l3_list.head


if __name__ == "__main__":
    # l1_list = LinkedList()
    # l1_list.append(9)
    # l1_list.append(9)
    # l1_list.append(9)
    # l1_list.append(9)
    # l1_list.append(9)
    # l1_list.append(9)
    # l1_list.append(9)
    #
    # l2_list = LinkedList()
    # l2_list.append(9)
    # l2_list.append(9)
    # l2_list.append(9)
    # l2_list.append(9)

    l1_list = LinkedList()
    l1_list.append(9)
    l1_list.append(8)

    l2_list = LinkedList()
    l2_list.append(1)

    sol = Solution()
    sol.add_two_numbers(l1_list.head, l2_list.head)