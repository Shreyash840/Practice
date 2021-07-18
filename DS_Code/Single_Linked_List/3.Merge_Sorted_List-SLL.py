from util.Single_Linked_List.SLL_base_util import newline, LinkedList, Node, print_linked_list


class MergeSortedlist:
    def __init__(self):
        self.dummy_head = None
        self.dummy_itr = None

    def new_sorted_list(self, node: Node):

        if self.dummy_head is None:
            self.dummy_head = self.dummy_itr = node

        else:
            while self.dummy_itr.next is not None:
                self.dummy_itr = self.dummy_itr.next

            self.dummy_itr.next = node

    def compare(self, list_head_1, list_head_2):
        head_itr_1 = list_head_1
        head_itr_2 = list_head_2

        while True:
            if head_itr_1 is None:
                self.new_sorted_list(node=head_itr_2)
                break

            if head_itr_2 is None:
                self.new_sorted_list(node=head_itr_1)
                break

            if head_itr_1.data >= head_itr_2.data:
                node = Node(data=head_itr_2.data)
                self.new_sorted_list(node=node)
                head_itr_2 = head_itr_2.next

            else:
                node = Node(data=head_itr_1.data)
                self.new_sorted_list(node=node)
                head_itr_1 = head_itr_1.next

    def print_list(self):
        if self.dummy_head is None:
            print("Empty List")
        else:
            self.dummy_itr = self.dummy_head

            while self.dummy_itr is not None:
                print(self.dummy_itr.data, sep=' ', end='-->')
                self.dummy_itr = self.dummy_itr.next


def in_place_merge(head_1, head_2):
    itr_1 = head_1
    itr_2 = head_2
    dummy_itr = dummy_head = Node(data=-1)

    while itr_1 and itr_2:
        if itr_1.data <= itr_2.data:
            dummy_itr.next = itr_1
            itr_1 = itr_1.next
            dummy_itr = dummy_itr.next
        else:
            dummy_itr.next = itr_2
            itr_2 = itr_2.next
            dummy_itr = dummy_itr.next

    if itr_1 is None:
        dummy_itr.next = itr_2
    if itr_2 is None:
        dummy_itr.next = itr_1

    return dummy_head.next


obj1 = LinkedList()
obj1.append_at_first(4)
obj1.append_at_first(2)
obj1.append_at_last(18)
obj1.append_at_last(19)
obj1.append_at_last(20)
obj1.print_linked_list()
print(newline)
obj2 = LinkedList()
obj2.append_at_first(4)
obj2.append_at_first(3)
obj2.append_at_first(1)
obj2.append_at_last(18)
obj2.append_at_last(25)
obj2.print_linked_list()
print(newline)
"""METHOD 1, making a new list"""
# merge_obj = MergeSortedlist()
# merge_obj.compare(obj1.head, obj2.head)
# merge_obj.print_list()
print(newline)

"""METHOD 2, in place method"""
print_linked_list(head=in_place_merge(obj1.head, obj2.head))
