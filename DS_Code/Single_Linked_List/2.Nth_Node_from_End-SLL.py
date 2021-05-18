from util.Single_Linked_List.SLL_base_util import LinkedList, newline


def get_nth_node_from_last(head_ref, n):
    main_node = itr_node = head_ref
    nth_node_count = n
    while itr_node.next is not None and n != 1:
        itr_node = itr_node.next
        n -= 1

    if n != 1:
        print("Total number of elements in the list is less than the count from the end")
        return

    while itr_node.next is not None:
        itr_node = itr_node.next
        main_node = main_node.next

    print(f"Data in the node from the {nth_node_count}th node from end is- {main_node.data}")


obj = LinkedList()
obj.append_at_first(7)
obj.append_at_first(6)
obj.append_at_first(5)
obj.append_at_first(4)
obj.append_at_last(8)
obj.append_at_last(9)
obj.append_at_last(10)
obj.print_linked_list()
print(newline)
get_nth_node_from_last(obj.head, 5)
get_nth_node_from_last(obj.head, 1)
get_nth_node_from_last(obj.head, 7)
get_nth_node_from_last(obj.head, 9)
