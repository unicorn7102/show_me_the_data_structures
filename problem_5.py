import hashlib
from datetime import datetime

class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        
    def calc_hash(self):
        sha = hashlib.sha256()

        hash_str = self.data.encode('utf-8')
        sha.update(hash_str)

        return sha.hexdigest()
    
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class BlockChain:
    
    def __init__(self, head=None):
        self.head = head
        self.tail = head
        self.size = 0
        
    def insert(self, new_data):
        if self.head is None:
            block = Block(datetime.now(), new_data, '0')
            self.head = Node(block)
            self.tail = self.head
        else:
            block = Block(datetime.now(), new_data, self.tail.value.hash)
            self.tail.next = Node(block)
            self.tail = self.tail.next
        self.size += 1
        
    def __repr__(self):
        node = self.head
        i = 0
        output = ''
        while node:
            block = node.value
            output += '-'*30
            output += '\n'
            output += f'Block {i}\n'
            output += f'timestamp: {block.timestamp}\n'
            output += f'data: {block.data}\n'
            output += f'hash: {block.hash}\n'
            output += f'previous_hash: {block.previous_hash}\n'
            
            node = node.next
            i += 1
        return output
    
if __name__=='__main':
    
    blockchain = BlockChain()

    blockchain.insert("some information")

    blockchain.insert("new information")

    print(blockchain)