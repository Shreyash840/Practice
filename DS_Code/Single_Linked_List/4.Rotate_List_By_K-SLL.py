from util.Single_Linked_List.SLL_base_util import newline, LinkedList, Node, print_linked_list


def rotate_list(head_1, k):
    length_node = itr_node= head_node = head_1
    length = 0

    if head_node==None or head_node.next == None or k==0:
        return head_node

    while length_node is not None:
        length = length + 1
        length_node = length_node.next
    if k >= length:
        k = k % length

    for _ in range(0, k):
        while itr_node.next is not None:
            prev_node = itr_node
            itr_node = itr_node.next

        itr_node.next = head_node
        prev_node.next = None
        head_node = itr_node
    return head_node


"""DRIVER CODE"""
obj = LinkedList()
# obj.append_at_first(4)
# obj.append_at_first(2)
obj.append_at_last(0)
obj.append_at_last(1)
obj.append_at_last(2)
# obj.append_at_last(4)
# obj.append_at_last(5)
obj.print_linked_list()
print(newline)
#----------------------#


"""MAIN CODE"""

list = rotate_list(head_1=obj.head, k=4)

print_linked_list(head=list)

