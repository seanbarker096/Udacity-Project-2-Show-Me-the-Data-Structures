## BlockChain

This solution uses a reversed linked list, where our starting reference point of the linked list is the tail as opposed to the head. This allows us to append to the blockchain in O(1) time via the`BlockChain.append` method.

The reference to previous blocks in the chain is implemented using as hash-map. The hash-map stores references to each node in the blockchain, with the blocks hash value used as the key. This allows us to traverse the blockchain by accessing the hashes from the `Block.previous_hash` property, which can be used to get the reference to the previous `Block` by looking it up in the hash-map. This allows us to access any block in the chain in constant time.

## Time Complexity

We can add to the block using `BlockChain.append` in constant time, and can access previous blocks in the chain in constant time using the has map. Overall the solution is therefore O(1)

## Space complexity

The space complexity of the solution is O(n) because the hash-map and linked list grows linearly with the number of blocks in the chain
