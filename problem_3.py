import sys
from collections import deque


##simple test helper function
def test(msg,expectation, comparison):
    if expectation == comparison:
        return print(f"{msg}: Passed")
    return print(f"{msg}: Failed")


def throws_err(fn):
    try:
        fn()
        return False
    except:
        return True


##classes
class Node():
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.visited_right_child = False
        self.visited_left_child = False
        self.parent = None

    def set_value(self,value):
        self.value = value

    def set_right_child(self, rchild):
        self.right_child = rchild

    def set_left_child(self, lchild):
        self.left_child = lchild
    
    def set_visited_left(self):
        self.visited_left_child = True

    def set_visited_right(self):
        self.visited_right_child = True

    def set_char_count(self, count):
        self.char_count = count

    def has_children(self):
        if self.left_child and self.right_child:
            return True
        return False


class Huffman_Node(Node):
    def __init__(self, value=None, character = None, lchild=None, rchild=None,):
        Node.__init__(self, value)
        self.character = character
        self.left_child = lchild
        self.right_child = rchild
        self.value = lchild.value + rchild.value  if (lchild and rchild) else value
    
    

def get_char_frequencies(data):
    ##returns dictionary of character counts
    if not isinstance(data, str):
        raise TypeError("Input to get_char_frequencies must be a string")
    char_counts = {}

    for char in data:
        char_counts[char] = char_counts.get(char,0) + 1;
    
    return char_counts


def create_sorted_node_queue(node_list):
    return deque(sorted(node_list, key = lambda node : node.value))


def build_huffman_tree(priority_queue):
    ##build the huffman tree
    while len(priority_queue) > 1:
        ##pop off first 2 elements
        lchild = priority_queue.popleft()
        rchild = priority_queue.popleft()
        
        new_huffman_node = Huffman_Node(lchild =  lchild,rchild = rchild)
        lchild.parent = new_huffman_node
        rchild.parent = new_huffman_node
      
        priority_queue.appendleft(new_huffman_node)
        
        priority_queue = create_sorted_node_queue(priority_queue)

    ##get table of binary codes for each character
    return priority_queue


def traverse_huffman_tree(root):
    binary_codes = {}
     ##handle edge case where tree contains single node
    if root and not root.left_child and not root.right_child:
        binary_codes[root.character] = (root.value, "0")
        return binary_codes
    node = root
    binary_str = ''
  
    while node:
       
        if node.left_child and not node.visited_left_child:
            binary_str += '0'
            node.visited_left_child = True
            node = node.left_child
            continue
        if node.right_child and not node.visited_right_child:
            binary_str += '1'
            node.visited_right_child = True
            node=node.right_child
            continue

        ##could be parent visted already, or not visisted child
        binary_codes[node.character] = (node.value, binary_str)
        binary_str = binary_str[0:-1]
        node = node.parent

    return binary_codes


def huffman_encoding(data):

    if not isinstance(data, str):
        raise TypeError("Input must be a string")
    
    char_frequencies = get_char_frequencies(data)

    priority_queue = deque([])
    nodes = []
    ##create the unsorted list first
    for char, count in char_frequencies.items():
        nodes.append(Huffman_Node(value=count,character = char))

    priority_queue = create_sorted_node_queue(nodes)

    huffman_tree = build_huffman_tree(priority_queue)
    ##if empty tree then give root default value of empty array
    huffman_tree_root = huffman_tree[0] if len(huffman_tree) > 0 else []
    huffman_binary_codes = traverse_huffman_tree(huffman_tree_root)
    
    ##create encoded string
    encoded_str = ''
    for char in data:
        # character_count = huffman_binary_codes[char][0]
        binary_code = huffman_binary_codes[char][1]
        encoded_str += binary_code

    return (encoded_str, huffman_tree)

def huffman_decoding(data,tree):
    root = tree[0] if len(tree) > 0 else []
    node = root
    encoded_string = data
    decoded_string = ''

    ##handle edge case of tree with depth 1
    if root and not root.has_children():
        for char in encoded_string:
            decoded_string  += root.character
        return decoded_string
        
    while encoded_string:
        ##always strip off a character from encoded string after loop iteration if not root
        if node != root:
            encoded_string = encoded_string[1:]

        ##once hits root add to encoded string
        if not node.has_children():
            decoded_string += node.character
            node = root
            continue
        if encoded_string[0] == "1":
            ##if current node has right child then traverse down to it 
            ##and remove character from encoded string
            if (node.right_child):
                node = node.right_child
  
        if encoded_string[0] == "0":
            if (node.left_child):
                node = node.left_child

    return decoded_string            

####################################################################################################
##tests

# ##test get_char_frequency
# test("Should return dict with correct character counts", True, get_char_frequencies('AAA')['A'] == 3)
# test("Should return dict with correct character counts", True, get_char_frequencies('AAABB')['A'] == 3 and get_char_frequencies('AAABB')['B'] == 2)
# test("Should return dict with correct character counts", True, get_char_frequencies('') == {})

# ## test create sorted queue
# test_list = [Huffman_Node(3,'A'), Huffman_Node(5,'B'),Huffman_Node(5,'Z'), Huffman_Node(1,'D')]
# test("Should return a queue where each element is a node sorted by their value property", True, (create_sorted_node_queue(test_list)[0]).character == 'D')
# test("Should return a queue where each element is a node sorted by their value property", True, (create_sorted_node_queue(test_list)[1]).character == 'A')
# test("Should return a queue where each element is a node sorted by their value property", True, (create_sorted_node_queue(test_list)[2]).character == 'B')
# test("Should return a queue where each element is a node sorted by their value property", True, (create_sorted_node_queue(test_list)[3]).character == 'Z')

# test_list2 = []

# test("Should return empty queue if list empty", True, create_sorted_node_queue(test_list2) == deque([]))

# ##TEST HUFFMAN ENCODING

# test_queue = create_sorted_node_queue([Huffman_Node(7,'A'), Huffman_Node(3,'B'),Huffman_Node(7,'C'), Huffman_Node(2,'D'),Huffman_Node(6,'E')])
# test("Should return queue of length 1", True, len(build_huffman_tree(test_queue))==1)


# huffman_tree = build_huffman_tree(test_queue)
# print(huffman_tree[0].right_child.value)
# print(huffman_tree[0].left_child.value)
# test("Nodes should contain the correct value properties", True, huffman_tree[0].right_child.value == 14 and huffman_tree[0].left_child.value == 11 )
# test("Nodes should contain the correct value properties", True, huffman_tree[0].left_child.left_child.value == 5 and huffman_tree[0].left_child.right_child.value == 6 )
# test("Nodes should contain the correct value properties", True, huffman_tree[0].left_child.left_child.left_child.value == 2 and huffman_tree[0].left_child.left_child.right_child.value == 3 )

# test("Nodes should contain the correct character properties", True, huffman_tree[0].right_child.character == None and huffman_tree[0].left_child.character == None )
# test("Nodes should contain the correct character properties", True, huffman_tree[0].left_child.left_child.character == None and huffman_tree[0].left_child.right_child.character == "E" )
# test("Nodes should contain the correct character properties", True, huffman_tree[0].left_child.left_child.left_child.character == "D" and huffman_tree[0].left_child.left_child.right_child.character == "B" )

# test_queue = create_sorted_node_queue([])
# huffman_tree = build_huffman_tree(test_queue)
# test("should return empty tree if no string passed in", True, len(huffman_tree)==0)

# test_queue = create_sorted_node_queue([Huffman_Node(5,'A')])
# huffman_tree = build_huffman_tree(test_queue)
# test("should return tree with one node, if only single character passed in", True, len(huffman_tree) ==1)

# wrapped_huffman = lambda x: build_huffman_tree(2132123)
# test("should throw error if string isnt passed in", True, throws_err(wrapped_huffman)==True)


## full integration test of huffman_encoding and decoding
test("should return corrrect encoded string", True,huffman_encoding('AAAAAAABBBCCCCCCCDDEEEEEE')[0] == "1010101010101000100100111111111111111000000010101010101")
test("should return empty encoded string if no characters are passed in", True, huffman_encoding("")[0] == "")

encoded_string, tree = huffman_encoding('AAAAAAABBBCCCCCCCDDEEEEEE')
print(huffman_decoding(encoded_string, tree) )
test("should return the original string", True, huffman_decoding(encoded_string, tree) =='AAAAAAABBBCCCCCCCDDEEEEEE' )

encoded_string, tree = huffman_encoding("")
test("should return the oroginal string", True, huffman_decoding(encoded_string, tree)=="")

encoded_string, tree = huffman_encoding("AAA")
test("should return the oroginal string", True, huffman_decoding(encoded_string, tree)=="AAA")

encoded_string, tree = huffman_encoding('The bird is the word')
test("should return the original string", True, huffman_decoding(encoded_string, tree) =='The bird is the word')

encoded_string, tree = huffman_encoding('A     test   setenence.')
test("should return the original string", True, huffman_decoding(encoded_string, tree) =='A     test   setenence.')

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
