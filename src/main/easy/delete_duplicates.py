# Given the head of a sorted linked list,
# delete all duplicates such that each element appears only once.
# Return the linked list sorted as well.
# Example-
# Input: head = [1,1,2,3,3]
# Output: [1,2,3]

# Definition for singly-linked list.
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

    def delete_duplicates(self):
        if self.head is None:
            return
        current = self.head
        while current.next is not None:
            if current.val == current.next.val:
                temp = current.next.next
                current.next = None
                current.next = temp
            else:
                current = current.next
        return self.head


if __name__ == "__main__":
    l1 = LinkedList()
    l1.append(0)
    l1.append(1)
    l1.append(2)
    l1.append(2)

    l1.delete_duplicates()
    l1.print_list()

