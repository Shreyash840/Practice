from util.Single_Linked_List.SLL_base_util import LinkedList, newline


class SLLLoopDetect:
    def __init__(self):
        self.linked_list_obj = LinkedList()
        self.linked_list_obj_test = LinkedList()

    def create_single_list_loop(self):
        self.linked_list_obj.append_at_first(7)
        self.linked_list_obj.append_at_first(6)
        self.linked_list_obj.append_at_first(5)
        self.linked_list_obj.append_at_last(8)
        self.linked_list_obj.append_at_last(9)
        self.linked_list_obj.append_at_last(10)
        self.linked_list_obj.head.next.next.next.next.next.next = self.linked_list_obj.head.next.next
        print("Base Code for creating single linked list with a loop is executed")
        print(newline)

    def create_single_list_without_loop(self):
        self.linked_list_obj_test.append_at_first(7)
        self.linked_list_obj_test.append_at_first(6)
        self.linked_list_obj_test.append_at_first(5)
        self.linked_list_obj_test.append_at_last(8)
        self.linked_list_obj_test.append_at_last(9)
        self.linked_list_obj_test.append_at_last(10)
        print("Base Code for creating single linked list without a loop is executed")
        self.linked_list_obj_test.print_linked_list()
        print(newline)

    @staticmethod
    def detect_loop(linked_list: LinkedList):
        slow_ptr = fast_ptr = linked_list.head

        while slow_ptr and fast_ptr:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
            if slow_ptr == fast_ptr:
                return True

        return False


obj = SLLLoopDetect()
obj.create_single_list_without_loop()
obj.create_single_list_loop()

if obj.detect_loop(linked_list=obj.linked_list_obj):
    print("loop exists")
else:
    print("loop doesn't exist")

if obj.detect_loop(linked_list=obj.linked_list_obj_test):
    print("loop exists")
else:
    print("loop doesn't exist")
