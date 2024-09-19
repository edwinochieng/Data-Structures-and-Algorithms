def reorderList(self, head):
    slow = head
    fast = head.next

    #split into two
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    
    #Reverse second half
    second = slow.next   #beginning of the second half of the list
    slow.next = None
    prev = None
    while second:
        temp = second.next
        second.next = prev
        prev = second
        second = temp

    #merge the two halves
    first = head
    second = prev
    while second:
        temp1 = first.next
        temp2 = second.next
        first.next = second
        second.next = temp1
        first = temp1
        second = temp2




