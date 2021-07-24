# Active Directory

This solution uses a Stack and Depth First Traversal, along with a `Group State` class. The stack allows us to navigate through the tree in O(n) time, whilst the `Group State` class helps to keep track of when parents have been visited already, and when all of their child groups have been visited.

## Time complexity

The tree traversal is completed in O(n) time due to the while loop inside of `is_user_in_group`. 

However, within this traversal there is a call to `user_is_in_current_group`. For each group we have to loop through all members in the `group.users` array to see if the user is in the group. This is done via the `user in groups` statement, which involves a loop of O(n).

Hence overall this nested loop makes the solution O(n^2).

## Space Complexity

This solution is O(n) in terms of space complexity as the stack grows linearly with number of sub_groups. 