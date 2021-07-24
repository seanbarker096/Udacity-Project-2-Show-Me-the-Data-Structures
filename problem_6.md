# Union and Intersection

## Union

### Time complexity

This uses two simple while loops, first looping over the first linked list and then the second. We keep track of visisted nodes by storing them in the `union_nodes` hash-map, meaning we can check if a node has already been added to the union in constant time.

If a node is not present in the new `union_llist` then it can be added in constant time using the `.append` method of the linked list. It therefore has time complexity of O(n).

### Space complexity

We create a new linked list to store the union making the solution O(n).

## Intersection

### Time complexity

Again this uses a simple while loop to loop over the two linked lists, only adding nodes to the new `intersection_list` if they are present in the first and second linked lists, and are not already present in the `intersection_list`. As `intersection_list` is itself a linked list, nodes can be appended in constant time.

We keep track of all nodes in the first linked list using a hash-map, meaning we can check for nodes occuring in both linked lists in constant time inside our second while loop, by referencing the current node in the second loop and checking for that key in the hash-map.

Due to the two while loops the overall solution is O(n) in terms of time complexity.

### Space complexity

We create a new linked list, as well as two hash-maps to keep track of nodes that are in the first linked list, as well as nodes that are in the intersection linked list (in order to avoid duplicate entries.)

The linked list and hash-maps increase as the number of entries in the two linked lists increase, making it O(n) in terms of space complexity.
