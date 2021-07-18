## adding el to cache (put/set) as well as getting it from cache (get) both count as operations

##if cache miss and cache full then add to cache

##least recently used -> i.e. even if op1 used once and all others at least 2x, if op2 was used 2x
##but was 10 years ago, then need to remove that one

##need to identify which item hasnt been used for longest period of time.

##could just use dictionary with key and value is time of last use. (just add date.now on put operation)

##doubly linked list
    ## -- tail will keep track of most recently used value in cache, head the oldest
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
            return
        ##add new node to tail

        self.tail.next = DoubleNode(value)
        self.tail.next.previous = self.tail
        self.tail = self.tail.next
        return
        
    def pop(self):
        ##remove head of list (least recently used)
        if self.head == None:
            return None

        node = self.head
        self.head = node.next
        
        return
        
            
        
        

        


##doubly linked list
  ##head keeps track of most recent
  ##When we need to remove oldest we just access the tail which we have a reference to already and move tail to next in list.
  ##Then just have to add new entry to replace it as the new head.

  ##If need to move item in middle of list up then just need to perform one operation to update next of preceding el to current els subsequent one. Then 
  ##one more operation to move next of subsquenbt to reference the preceding node.
  ##Then need to make previous head reference moved element as its next, and moved element to reference old head as other next

  ##also need to keep reference to position in the list inside the hash map. OR just store the node inside the hashmap so can access it directly using key

  #   ##Use dictionary   

def test(msg,expectation, comparison):
    if expectation == comparison:
        return print(f"{msg}: Passed")
    return print(f"{msg}: Failed")

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.cache = dict(zip([i for i in range(1, capacity +1)], [[None, None] for i in range(1, capacity +1)]));
        self.capacity = capacity;
        self.size = 0;
        ##keep list stored internally where start of list is most recently used, and start is least
        ##when need to remove least recently used just pull element from start of stack/list
        ##so we want a queue (last in last out, first in first out)
        self.order_of_use =  list();

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        pass

    def set(self, key, value):
        if self.size:
            # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
            self.cache[key][0] = value
            #store utc time so all are comparable
            self.cache[key][1] = datetime.now(timezone.utc)
            self.order_of_use.append(key)
        ##if full then remove least recently used

     

our_cache = LRU_Cache(5)

our_cache.set(1, 1);
test("Should correctly set value into cache",True, our_cache.cache[1][0] == 1);
test("Should correctly store a datetime object to represent time added to cache",True, isinstance(our_cache.cache[1][1], datetime))

our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);

##test value added to cache correctly

##test first entry date greater than second

# our_cache.get(1)       # returns 1
# our_cache.get(2)       # returns 2
# our_cache.get(9)      # returns -1 because 9 is not present in the cache

# our_cache.set(5, 5) 
# our_cache.set(6, 6)

# our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
