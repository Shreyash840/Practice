from util.Single_Linked_List.SLL_base_util import newline, LinkedList


def create_merge(head_1, head_2):
    itr_1 = head_1
    itr_2 = head_2

    while itr_2.data != 8:
        itr_2 = itr_2.next

    while itr_1.next.data != 8:
        itr_1 = itr_1.next

    itr_1.next = itr_2

    return head_1, head_2


def find_intersect(head_1, head_2):
    """"""
    itr_1 = head_1
    itr_2 = head_2
    pass_1 = pass_2 = True

    while itr_1 != itr_2:

        itr_2 = itr_2.next
        itr_1 = itr_1.next

        if itr_1 is None:
            if pass_1:
                itr_1 = head_2
                pass_1 = False
            else:
                return None
        if itr_2 is None:
            if pass_2:
                itr_2 = head_1
                pass_2 = False
            else:
                return None

    return itr_1.data


"""DRIVER CODE"""
obj1 = LinkedList()
obj1.append_at_last(4)
obj1.append_at_last(1)
obj1.append_at_last(8)
obj1.append_at_last(4)
obj1.append_at_last(5)
obj1.print_linked_list()
print(newline)
obj2 = LinkedList()
obj2.append_at_last(5)
obj2.append_at_last(6)
obj2.append_at_last(1)
obj2.append_at_last(8)
obj2.append_at_last(4)
obj2.append_at_last(5)
obj2.append_at_last(17)
obj2.append_at_last(22)
obj2.print_linked_list()
print(newline)

obj1.head, obj2.head = create_merge(obj1.head, obj2.head)
# ----------------------#

"""MAIN CODE"""
res = find_intersect(head_1=obj1.head, head_2=obj2.head)
print(res)
