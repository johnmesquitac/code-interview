'''class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next'''

#check if a linked list is palindrome

def check_palindrome_linked_list(head):
    slow=fast=head

    #finding the middle of the list
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    
    #reversing the right portion of the list
    past = None
    while slow:
        temp = slow
        slow = slow.next
        temp.next = past
        past = temp
    
    #checking palindrome
    left = head
    right = past

    while right:
        if right.val!=left.val:
            return False
        right = right.next
        left = left.next

    return True
    