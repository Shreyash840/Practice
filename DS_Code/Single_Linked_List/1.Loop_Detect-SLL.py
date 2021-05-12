from util.Single_Linked_List.SLL_base_util import LinkedList, Node, newline


class SLLLoopDetect:
    def __init__(self):
        self.linked_list_obj = LinkedList()
        self.linked_list_obj_test = LinkedList()

    def create_single_list_loop(self):
        self.linked_list_obj.append_at_first(7)
        self.linked_list_obj.append_at_first(6)
        self.linked_list_obj.append_at_first(5)
        self.linked_list_obj.append_at_first(4)
        self.linked_list_obj.append_at_last(8)
        self.linked_list_obj.append_at_last(9)
        self.linked_list_obj.append_at_last(10)
        self.linked_list_obj.head.next.next.next.next.next.next = self.linked_list_obj.head.next.next
        print("Base Code for creating single linked list with a loop is executed")

    def create_single_list_without_loop(self):
        self.linked_list_obj_test.append_at_first(7)
        self.linked_list_obj_test.append_at_first(6)
        self.linked_list_obj_test.append_at_first(5)
        self.linked_list_obj_test.append_at_last(8)
        self.linked_list_obj_test.append_at_last(9)
        self.linked_list_obj_test.append_at_last(10)
        print("Base Code for creating single linked list without a loop is executed", end='')
        # self.linked_list_obj_test.print_linked_list()
        print(newline)

    def detect_loop(self, linked_list: LinkedList):
        slow_ptr = fast_ptr = linked_list.head

        while slow_ptr and fast_ptr:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
            if slow_ptr == fast_ptr:
                count = self.count_element_in_loop(node=slow_ptr)
                return count, True

        return 0, False

    @staticmethod
    def count_element_in_loop(node: Node):
        value_at_intersection_node = node.data
        count = 0

        while node:
            node = node.next
            count += 1
            if node.data == value_at_intersection_node:
                break

        return count


obj = SLLLoopDetect()
obj.create_single_list_loop()
obj.create_single_list_without_loop()

res = obj.detect_loop(linked_list=obj.linked_list_obj)

obj.linked_list_obj_test.print_linked_list()
print(newline)
res_test = obj.detect_loop(linked_list=obj.linked_list_obj_test)

if res[1]:
    print("loop exists, no. of elements in loop is - ", res[0])
else:
    print("loop doesn't exist")

if res_test[1]:
    print("loop exists")
else:
    print("loop doesn't exist, no. of elements in loop is - ", res_test[0])
