class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Your Solution Here
    added = {}
    union = LinkedList()
    
    node = llist_1.head
    while node:
        val = node.value
        count = added.get(val, 0)
        if count == 0: 
            union.append(val)
            added[val] = 1
        node = node.next
    
    node = llist_2.head
    while node:
        val = node.value
        count = added.get(val, 0)
        if count == 0: 
            union.append(val)
            added[val] = 1
        node = node.next
    
    return union

def intersection(llist_1, llist_2):
    # Your Solution Here
    added = {}
    intersection = LinkedList()
    
    node = llist_1.head
    while node:
        val = node.value
        count = added.get(val, 0)
        if count == 0: 
            added[val] = 1
        node = node.next
    
    node = llist_2.head
    while node:
        val = node.value
        count = added.get(val, 0)
        if count == 1: 
            intersection.append(val)
            added[val] += 1
        node = node.next
        
    return intersection

if __name__ == '__main':
    
    # Test case 1

    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3,2,4,35,6,65,6,4,3,21]
    element_2 = [6,32,4,9,6,1,11,21,1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print (union(linked_list_1,linked_list_2))
    # 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 21 -> 32 -> 9 -> 1 -> 11 -> 
    print (intersection(linked_list_1,linked_list_2))
    # 6 -> 4 -> 21 -> 

    # Test case 2

    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3,2,4,35,6,65,6,4,3,23]
    element_2 = [1,7,8,9,11,21,1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print (union(linked_list_3,linked_list_4))
    # 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 ->
    print (intersection(linked_list_3,linked_list_4))
    # ''

    # Test case 3

    linked_list_5 = LinkedList()
    linked_list_6 = LinkedList()

    element_1 = []
    element_2 = []

    for i in element_1:
        linked_list_5.append(i)

    for i in element_2:
        linked_list_6.append(i)

    print (union(linked_list_5,linked_list_6))
    # ''
    print (intersection(linked_list_5,linked_list_6))
    # ''