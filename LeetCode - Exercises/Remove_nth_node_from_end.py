'''Given the head of a linked list, remove the nth node from the end of the list
 and return its head.'''

def remove_nth_node(head, n):
    slow=fast=head
    while n>0:
        fast=fast.next
        n-=1
    if fast is None:
        return head.next
    while fast and fast.next:
        fast = fast.next
        slow= slow.next
    slow.next = slow.next.next
    return head