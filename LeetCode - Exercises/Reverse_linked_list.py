
#Given the head of a singly linked list, reverse the list and return the reversed list

'''class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next'''

def reverse_linked_list(head):
    past = None
    while head:
        temp = head
        head = head.next
        temp.next = past
        past = temp
    return past