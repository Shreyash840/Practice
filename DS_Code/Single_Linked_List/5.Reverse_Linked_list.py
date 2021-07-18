from util.Single_Linked_List.SLL_base_util import newline, LinkedList, print_linked_list


def reverse_list(head):
    prev = None
    curr = head

    while curr is not None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev


def rev_recursion(head):
    if head is None or head.next is None:
        return head

    rev_head = rev_recursion(head.next)
    temp = head
    head.next.next = temp
    head.next = None
    return rev_head


"""DRIVER CODE"""
obj = LinkedList()
# obj.append_at_first(4)
# obj.append_at_first(2)
# obj.append_at_last(0)
obj.append_at_last(1)
obj.append_at_last(2)
obj.append_at_last(3)
# obj.append_at_last(5)
obj.print_linked_list()
print(newline)
# ----------------------#


"""MAIN CODE"""
rev_list = rev_recursion(head=obj.head)

print_linked_list(head=rev_list)
