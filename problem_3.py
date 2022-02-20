# coding: utf-8

import sys

class TreeNode(object):
    def __init__(self, char=None, freq=None):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
        
    def set_left_child(self,left):
        self.left = left
        
    def set_right_child(self, right):
        self.right = right
        
    def get_left_child(self):
        return self.left
    
    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None
    
    def has_right_child(self):
        return self.right != None

class Tree(object):
    def __init__(self, root=None):
        self.root = root
        
    def get_root(self):
        return self.root
    
    def set_root(self, root):
        self.root = root
        
    def get_paths(self):
        root = self.get_root()
        
        def _get_paths(node):
            paths = []
            if node.has_left_child():
                left_path = _get_paths(node.get_left_child())
                if len(left_path):
                    paths.extend(['0'+s for s in left_path])
                else:
                    paths.extend(['0'])
            
            if node.has_right_child():
                right_path = _get_paths(node.get_right_child())
                if len(right_path):
                    paths.extend(['1'+s for s in right_path])
                else:
                    paths.extend(['1'])
            return paths
            
        return _get_paths(root)
    
    def get_leaf_by_path(self, path):
        node = self.get_root()
        for bit in path:
            if bit == '0':
                node = node.get_left_child()
            else:
                node = node.get_right_child()
        return node
        
class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
class LinkedList(object):
    def __init__(self):
        self.head = None
        
    def pop(self):
        if self.head is None:
            return None
        
        pop_node = self.head.data
        self.head = self.head.next
        return pop_node
    
class PriorityQueue(object):
    def __init__(self):
        self.list = LinkedList()
        self.size = 0
        
    def deque(self):
        if self.size:
            self.size -= 1
            return self.list.pop()
        else:
            return None
    
    def insert(self, new_item):
        self.size += 1
        new_node = Node(new_item)
        
        if self.list.head is None:
            self.list.head = new_node
            return
        
        if new_node.data.freq < self.list.head.data.freq: 
            new_node.next = self.list.head
            self.list.head = new_node
            return
        
        node = self.list.head
        
        while node:
            if node.next is None:
                node.next = new_node
                break
            elif new_node.data.freq >= node.data.freq and new_node.data.freq < node.next.data.freq:
                new_node.next = node.next
                node.next = new_node
                break
            else:
                node = node.next          
                
    def __repr__(self):
        out = ""
        if self.list.head is None:
            return out
        node = self.list.head
        while node:
            out += f"Node({node.data.char} | {node.data.freq})\n"
            node = node.next
        return out
    
def get_char_freq_table(data):
    
    char_freq = dict()
    for c in data:
        if c in char_freq:
            char_freq[c] = char_freq[c] + 1
        else:
            char_freq[c] = 1
            
    return char_freq
        
def huffman_encoding(data):
    
    if data is None:
        return None, Tree()
    
    if len(data) == 0:
        tree = Tree()
        tree.set_root(TreeNode(char=""))
        return "", tree
    
    # First, determine the frequency of each character in the message. 
    char_freq = get_char_freq_table(data)
                      
    # build and sort a list of nodes in the order lowest to highest frequencies.
    p_queue = PriorityQueue()
    for char, freq in char_freq.items():
        new_node = TreeNode(char=char, freq=freq)
        p_queue.insert(new_node)
        
    # building of a Huffman tree.
    if p_queue.size == 1:
        tree = Tree()
        head_node = TreeNode(freq=p_queue.list.head.data.freq)
        head_node.set_left_child(p_queue.list.head.data)
        tree.set_root(head_node)
    else:
        while p_queue.size > 1:
            pop1 = p_queue.deque()
            pop2 = p_queue.deque()
            new_node = TreeNode(freq=pop1.freq+pop2.freq)
            new_node.set_left_child(pop1)
            new_node.set_right_child(pop2)

            p_queue.insert(new_node)

        tree = Tree(p_queue.list.head.data)
    
    # Based on the Huffman tree, generate unique binary code for each character.
    paths = tree.get_paths()
    code_map = dict()
    for path in paths:
        leaf = tree.get_leaf_by_path(path)
        code_map[leaf.char] = path
    
    # Generate the encoded data.
    encoded_data = ""
    for char in data:
        encoded_data += code_map[char]
        
    return encoded_data, tree

def huffman_decoding(data,tree):
    
    if data is None:
        return None
    
    decoded_data = ""
    
    node = tree.get_root()
    for bit in data:
        if bit == '0':
            node = node.get_left_child()
        elif bit == '1':
            node = node.get_right_child()
            
        if (not node.has_left_child()) and (not node.has_right_child()):
            decoded_data += node.char
            node = tree.get_root()
            
    return decoded_data

if __name__ == '__main__':
    
    ex1 = "The bird is the word"
    encoded, tree = huffman_encoding(ex1)
    decoded = huffman_decoding(encoded, tree)
    print(decoded)
    # The bird is the word
    
    ex2 = "DDDDD"
    encoded, tree = huffman_encoding(ex2)
    decoded = huffman_decoding(encoded, tree)
    print(decoded)
    # DDDDD
    
    ex3 = None
    encoded, tree = huffman_encoding(ex3)
    decoded = huffman_decoding(encoded, tree)
    print(decoded)
    # None