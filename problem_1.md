# Explanation

The solution uses a Doubly Linked List to store the cache entries, as it is the only linked list type that would allow us to access a node that isnt the head or tail, and remove or move it. By having a reference to the node before and after we can remove/move it in constant time. This provides the functionality we need to move items around so that the start of the list contains the Least Recently Used cache item.

In order to access items in the cache in constant time we can use a hash-map, where the value associated with any given key contains any given node in the Doubly Linked List.

## Overall time complexity

Overall all operations take O(n) time.

## Space complexity

Space complexity is O(n), where n would be the capacity of the cache. This is because the size of the hash-map and the length of the doubly linked list increases as the capacity of the cache increases.
