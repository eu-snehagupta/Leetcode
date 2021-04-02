# Merge two sorted linked lists and return it as a sorted list.
# The list should be made by splicing together the nodes of the first two lists.
#
# Example 1:
# Input: l1 = [1,2,4], l2 = [1,3,4]
# Output: [1,1,2,3,4,4]
#
# Constraints:
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both l1 and l2 are sorted in non-decreasing order.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_val):
        new_node = Node(new_val)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        if self.head is None:
            print("Empty list!")
            return
        current = self.head
        while current:
            print(current.val, end=" ")
            current = current.next


def merge_two_linked_lists(list1, list2):
    if list1 is None and list2 is None:
        return

    if list1 is None:
        return list2

    if list2 is None:
        return list1

    merged_linked_list = LinkedList()
    while not(list1 is None or list2 is None):
        if list1.val < list2.val:
            merged_linked_list.append(list1.val)
            list1 = list1.next
        else:
            merged_linked_list.append(list2.val)
            list2 = list2.next
    if list1 is None:
        while list2 is not None:
            merged_linked_list.append(list2.val)
            list2 = list2.next
    if list2 is None:
        while list1 is not None:
            merged_linked_list.append(list1.val)
            list1 = list1.next
    merged_linked_list.print_list()
    return merged_linked_list.head


if __name__ == '__main__':
    l1 = LinkedList()
    l1.append(1)
    l1.append(2)
    l1.append(4)

    l2 = LinkedList()
    l2.append(1)
    l2.append(3)
    l2.append(4)

    merge_two_linked_lists(l1.head, l2.head)