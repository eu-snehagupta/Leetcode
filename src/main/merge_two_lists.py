class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_data):
        new_node = Node(new_data)
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
            print(current.data, end=" ")
            current = current.next


# class Solution:
#    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
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
        merged_list.append(current.data)
        current = current.next

    current = list2
    while current is not None:
        merged_list.append(current.data)
        current = current.next

    merged_list.sort()
    for elements in merged_list:
        merged_linked_list.append(elements)

    merged_linked_list.print_list()
    print(merged_linked_list.head)


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