import hashlib
from datetime import datetime
from datetime import timezone, datetime
import json

class Block:
    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()
    
   
    def calc_hash(self):
        sha = hashlib.sha256()

        hash_str = (json.dumps(self.data) + f"{self.timestamp}").encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()


class BlockChain:
    def __init__(self):
        self.tail = None
        self.block_hash_map = {}

    def __get_block(self,hash):
        return self.block_hash_map.get(hash,None)

    def get_previous_block(self, current_block):
        return self.__get_block(current_block.previous_hash)

    def get_tail(self):
        return self.tail

    def __create_block(self, data, previous_hash):
        timestamp = datetime.now(timezone.utc)
        return Block(timestamp, data, previous_hash)


    def append(self, new_block_data):
        if self.get_tail():
            new_block = self.__create_block(new_block_data, self.tail.hash)
            ##new_block.previous_hash = self.__get_block(self.tail.hash).hash
            self.tail = new_block
        else:
            self.tail = self.__create_block(new_block_data, 0)

        ##add new block to hash_map
        self.block_hash_map[self.tail.hash] = self.tail

    def __repr__(self):
        block = self.get_tail()

        s = "______________BlockChain_________________________\n"
        s = s + "______________Tail_________________________\n"

        i = 1
        while block:
            s = s + f"Block {i}:\n    Block Data:{block.data}\n    Current hash: {block.hash}\n  Previous Hash: {block.previous_hash} "
            s = s + "_________________________________\n\n\n"
            block = self.get_previous_block(block)
            i+=1
        s = s + "______________Head_________________________\n"
        return s


block_chain = BlockChain()

block_data = { "username": "User 1", "total_funds_transferred": "$100", "item_id": 5, "transaction_id": "1"}
block_chain.append(block_data)
block_chain.append({ "username": "User 2", "total_funds_transferred": "$20", "item_id": 5, "transaction_id": "2"})
block_chain.append({ "username": "User 454", "total_funds_transferred": "$340", "item_id": 5, "transaction_id": "3"})
block_chain.append({ "username": "User 1", "total_funds_transferred": "$207", "item_id": 5, "transaction_id": "4"})

print(repr(block_chain))