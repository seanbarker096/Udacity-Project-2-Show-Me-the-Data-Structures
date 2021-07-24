## File recursion

This code uses Depth First Search, specifically Pre-Order traversal. This is implemented as a stack as it allows us to easily keep track of the bottom of branch we are visiting, as this node will simply be the top nnode in the stack. We can therefore easily pop this off. The next node below this will then be its parent. We can therefore easily then visit any other of its children, push them to the stack, and if they are leaf nodes, pop them off again.

We also track the state of each node via the `self.visited` property of the State class. This prevents us being caught in an infinte loop when visiting children nodes and then revisiting the parent once it is popped off the stack.

A list is used to keep track of all child nodes for a given parent - this allows us to efficiently visit all child nodes in O(n) time, as we can just pop each child from the list when it is visited, rather than looping over all children to check if it has the `visited` state property set to `True`.

## Time efficiency

The overall time efficiency of the code is O(n).

Traversing the tree using the `Stack` and `State` class implementations is done in O(n) time via depth first search and pre-order traversal.

The function `contains_suffix` is also O(n), where n is the length of the path to check for the suffix.

Other functions such as `get_formatted_path` are O(1).

This assumes that the `os` functions used are O(n) or O(1).
