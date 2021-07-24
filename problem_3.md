# Huffman Coding

This solution uses a priority queue using Pythons built in `deque` module, and subsequently builds a binary tree during the encoding process.

Using the priority queue allows us to remove the 2 lowest priority nodes from the queue in O(n) time due to the sorting process.

## Time complexity

Code has been added to get a reference to the node in the queue after the two nodes which are popped off. This allows a comparison of its value to the new huffman nodes value. If its value is still less than the next node in the queue, there is no need to resort the list. Although the sorting is still O(n), it has the potential to be far less expensive than if the queue was resorted by default everytime a huffman node was created.

Traversing the tree to create the binary codes for each character costs O(n) due to the while loop inside of the `traverse_huffman_tree` function.

Creating the encoded string inside of `huffman_encoding` is O(n) due to the for loop, where we loop over each character of the original string passed in to the function. We use a hash-map to store binary codes for each character which we created when traversing the tree so they can be looked up in constant time.

Decoding the string by traversing the tree is done in O(n) time due to the while loop.

## Space complexity

Overall the solution is O(n) in terms of space complexity due to things such as storing the encoded string, the hash-map with binary codes, and the tree nodes themselves - all of which scale linearly with n.
