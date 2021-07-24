def test(msg,expectation, comparison):
    if expectation == comparison:
        return print(f"{msg}: Passed")
    return print(f"{msg}: Failed")

class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, value):
        if self.head == None:
            self.head = DoubleNode(value);
            self.tail = self.head;
            ##need to return tail so can store node object in our hash table
            return self.tail;

        ##add new node to tail
        self.tail.next = DoubleNode(value)
        self.tail.next.previous = self.tail
        self.tail = self.tail.next
        return self.tail
        
    def pop(self):
        ##remove head of list (least recently used)
        if self.head == None:
            return None

        node = self.head
        self.head = node.next
        
        return node.value

    ## function assumes the node being passed in exists in the list so that operations are O(n)
    def move_to_tail(self, node):
        ##if already tail return (this covers case where have a single node so tail is also head)
        if self.tail == node:
            return self.tail
        ##if list empty return none
        if self.head == None:
            return 
        ##handle case where node is head
        if self.head == node:
            ##first remove head
            self.pop()
            ##now move node to tail
            self.append(node.value)
            return self.tail

        ##update nodes referencing current node
        node.next.previous = node.previous
        node.previous.next = node.next
        ##move to tail and return the new node we create
        return self.append(node.value)
          


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.cache = dict()
        self.size = 0
        self.capacity = capacity
        self.LRU_list = DoublyLinkedList()

    def get(self, key):
        ##check if key exists in hashmap.
        cache_entry = self.cache.get(key)

        if cache_entry:
            ##if it does we need to move it to the tail of the queue
            updated_cache_entry = self.LRU_list.move_to_tail(cache_entry)
            ##updated cache to reference new node in list
            self.cache[key]  = updated_cache_entry
            return updated_cache_entry.value

        return -1

    def set(self, key, value):
        ##check if already exists
        if self.cache.get(key):
            ## move to end of list
            cache_entry = self.LRU_list.move_to_tail(value)

        ##if doesnt exist, check if cache is at capacity
        if self.size == self.capacity:
              ##handle edge case where capacity of cache is 0
              if self.capacity == 0:
                  return None 
              ##if it is at capacity then remove get key of head from LRU_list and remove from cache
              head_key = self.LRU_list.head.value
              self.cache.pop(head_key)
              # Then remove head from list (pop) and append to tail (append)
              self.LRU_list.pop()
              cache_entry = self.LRU_list.append(value) 
            
        ##if there is space in cache and the key not already in there then append to list
        else:
            cache_entry =  self.LRU_list.append(value)
            self.size += 1 
        ##update actual cache
        self.cache[key] = cache_entry


############################################# TESTS ###############################################
##test doubly_linked list implementation

# test_list = DoublyLinkedList()
# test_node = DoubleNode(1)

# test("Empty list should return none for tail", True, test_list.tail == None)
# test("Empty list should return none for head", True, test_list.head == None)
# test("Pop should return None for empty list", True, test_list.pop() == None)
# test("Move_to_tail should return none for empty list", True, test_list.move_to_tail(test_node) == None)

# node1 = test_list.append(1)
# test("Append should add node to tail of list", True, test_list.tail.value  == 1)
# test("Move_to_tail should return the tail node for list with single node", True, test_list.move_to_tail(node1).value== node1.value)
# test("Pop should return head if list not empty", True, test_list.pop()== 1)

# node1 = test_list.append(1)
# node2 = test_list.append(2)
# test_list.move_to_tail(node1)
# test("Move_to_tail should move node to end of list if not empty", True, test_list.tail.value == 1 )


# test_list2 = DoublyLinkedList()
# node1 = test_list2.append(1)
# node2 = test_list2.append(2)
# node3 = test_list2.append(3)
# node4 = test_list2.append(4)
# test_list2.move_to_tail(node2)
# test("Move_to_tail should correctly update other nodes references", True, test_list2.head.next.value == 3)
# test("Move_to_tail should correctly update other nodes references", True, test_list2.head.next.previous.value == 1)
# test("Move_to_tail should move node to end of list if not empty", True, test_list2.tail.value == 2 )


##TEST CACHE
our_cache = LRU_Cache(5)

our_cache.set(1, 1);
test("Should correctly set value into cache",True, our_cache.cache[1].value == 1);

our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);
test("Should correctly set value into cache",True, our_cache.cache[4].value == 4);

test("Should return correct valuen from cache", True, our_cache.get(1) == 1)      # returns 1
# print("current tail", our_cache.LRU_list.tail.value)
# print("current head", our_cache.LRU_list.head.value)
test("Should return correct valuen from cache", True, our_cache.get(2) == 2)      # returns 2
# print("current tail", our_cache.LRU_list.tail.value)
# print("current head", our_cache.LRU_list.head.value)
test("Should return -1 if value doesnt exist in cache", True, our_cache.get(9) == -1)     # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)
test("Should remove Least Used Value from cache correctly",True, our_cache.get(3) == -1)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

##TEST EMPTY CACHE
our_cache2 = LRU_Cache(0)
our_cache2.set(1, 1) 
test("Cache with zero capacity should return None when access attempted",True,our_cache2.get(1) == -1) #should return -1 as cache capacity is zero


