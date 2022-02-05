#!/usr/bin/env python
# coding: utf-8

class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        
    def append(self, value):
        """ Append a value to the end of the list. """   
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            return
        self.tail.next = Node(value)
        self.tail = self.tail.next
    
    def remove(self, value):
        """ Remove first occurrence of value. """
        if self.head is None:
            return
        
        if self.head.value == value:
            self.head = self.head.next
            return

        node = self.head
        while node.next is not None:
            if node.next.value == value:
                node.next = node.next.next
                if node.next is None: 
                    self.tail = node
                return
            node = node.next

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.keyList = LinkedList()
        self.storage = dict()
        self.capacity = capacity
        self.size = 0
        
    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        val = self.storage.get(key, None)
        if val:
            self.keyList.remove(key)
            self.keyList.append(key)
            return val
        else:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if (key in self.storage) or (self.capacity<=0):
            return
        
        if self.size >= self.capacity:
            remove_key = self.keyList.head.value
            self.keyList.head = self.keyList.head.next
            del self.storage[remove_key]
            self.size -= 1
            
        self.storage[key] = value
        self.keyList.append(key)
        self.size += 1

def test_case1():
    '''Normal case'''
    output = []
    test = LRU_Cache(4)
 
    test.set(1, 1)
    test.set(2, 2)
    test.set(3, 3)
    test.set(4, 4)
    
    output.append(test.get(2)) # 2
    output.append(test.get(9)) # -1

    test.set(5, 5) 
    test.set(6, 6)

    output.append(test.get(1)) # -1
    output.append(test.get(3)) # -1
    output.append(test.get(6)) # 6
    
    return output

def test_case2():
    '''Edge case with zero capacity'''
    output = []
    test = LRU_Cache(0)

    test.set(1, 1)
    test.set(2, 2)

    output.append(test.get(1)) # -1
    output.append(test.get(2)) # -1
    
    return output

def test_case3():
    '''Edge case with empty cache'''
    output = []
    test = LRU_Cache(2)

    output.append(test.get(1)) # -1
    output.append(test.get(None)) # -1
    
    return output

if __name__ == '__main__':
    
    print(test_case1())
    # [2, -1, -1, -1, 6]

    print(test_case2())
    # [-1, -1]

    print(test_case3())
    # [-1, -1]




