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
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

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

    merged_list = []
    merged_linked_list = LinkedList()

    current = list1
    while current is not None:
        merged_list.append(current.val)
        current = current.next

    current = list2
    while current is not None:
        merged_list.append(current.val)
        current = current.next

    merged_list.sort()
    for elements in merged_list:
        merged_linked_list.append(elements)

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