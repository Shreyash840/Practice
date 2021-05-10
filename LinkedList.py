""" Linked List"""

newline = "\n-------------"


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append_at_first(self, data_to_insert):
        new_node = Node(data=data_to_insert)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def append_at_last(self, data_to_insert):
        new_node = Node(data=data_to_insert)

        if self.head is None:
            self.head = new_node
        else:
            itr_node = self.head

            while itr_node.next is not None:
                itr_node = itr_node.next

            itr_node.next = new_node

    def append_at_index(self, data_to_insert, index):
        pos = 0
        new_node = Node(data_to_insert)
        if self.head is None or index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        itr_node = self.head

        while itr_node.next is not None:
            pos += 1
            if pos == index:
                new_node.next = itr_node.next
                itr_node.next = new_node
                return
            itr_node = itr_node.next
        if itr_node.next is None:
            if pos + 1 < index:
                print("out of bound")
            else:
                itr_node.next = new_node

    def total_elements_in_linked_list(self):
        if self.head is None:
            count = 0
        else:
            count = 1
            itr_node = self.head
            while itr_node.next is not None:
                count += 1
                itr_node = itr_node.next
        return count

    def print_linked_list(self):
        itr_node = self.head

        if itr_node is None:
            print("Empty List")
            return

        while itr_node is not None:
            print(itr_node.data, sep=' ', end='-->')
            itr_node = itr_node.next

    def delete_at_beginning(self):
        if self.head is None:
            print("List is Empty")

        # temp_node = self.head //this code is not needed as there is no need to free the head
        self.head = self.head.next

        # temp_node = None //this code is not needed as there is no need to free the head


LinkedList_obj = LinkedList()

LinkedList_obj.append_at_first(5)
LinkedList_obj.append_at_first(7)
LinkedList_obj.append_at_first(11)
LinkedList_obj.print_linked_list()
print(newline)

LinkedList_obj.append_at_last(8)
LinkedList_obj.append_at_last(12)
LinkedList_obj.print_linked_list()
print(newline)

LinkedList_obj.append_at_index(data_to_insert=6, index=5)
LinkedList_obj.print_linked_list()
print(newline)

print("Total number of elements in list is", LinkedList_obj.total_elements_in_linked_list(), end='')
print(newline)

LinkedList_obj.delete_at_beginning()
LinkedList_obj.print_linked_list()
print(newline)
