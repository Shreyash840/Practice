class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        itr_node = self.head

        if self.head is None:
            self.head = new_node
            return

        while itr_node.next is not None:
            itr_node = itr_node.next

        itr_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node

    @staticmethod
    def count_elements_in_list(self, Linked_list):
        count = 0

        while Linked_list is not None:
            count += 1
            Linked_list = Linked_list.next

        return count

    def append_at_index(self, data, index):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        if index == 1:
            new_node.next = self.head
            self.head = new_node
            return

        length = self.count_elements_in_list(self, Linked_list=self.head)

        if index > length:
            print("Exceeds index for adding the element")
            return

        prev_node = self.head

        while (index - 1) > 1:
            prev_node = prev_node.next
            index -= 1

        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_from_beginning(self):
        temp_node = self.head

        if self.head is None:
            print("List is Empty")
            return

        self.head = self.head.next
        temp_node = None

    def print_list(self):
        itr_node = self.head

        if self.head is None:
            print("Empty List")
            return

        while itr_node is not None:
            print(itr_node.data, sep=' ', end='-->')
            itr_node = itr_node.next


llist = LinkedList()

llist.print_list()
llist.append_at_index(30, 1)
llist.print_list()
print("\n-------------")
llist.append_at_index(20, 2)
llist.print_list()
print("\n-------------")
llist.append_at_index(10, 3)
llist.print_list()
print("\n-------------")
llist.append_at_index(15, 3)
llist.print_list()
print("\n-------------")
llist.append_at_index(25, 2)
llist.print_list()
print("\n-------------")
llist.append_at_index(35, 1)
llist.print_list()
print("\n-------------")
llist.append(100)
llist.append(200)
llist.append(300)
llist.append(400)
llist.prepend(70)
llist.prepend(50)
llist.prepend(40)
llist.append(500)
llist.print_list()
print("\n-------------")
llist.delete_from_beginning()
llist.print_list()


