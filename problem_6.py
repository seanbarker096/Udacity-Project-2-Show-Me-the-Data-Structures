class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    # Your Solution Here
    union_nodes = {}
    union_llist = LinkedList()
    ##simply append one list to the other whilist removing duplicates
    node = llist_1.head
    while node:
        ##duplicate node in new linked list
        union_node = Node(node.value)
        ##if isnt already in union nodes then add, otherwise skip to next node
        if union_nodes.get(union_node.value,None):
            node = node.next
            continue
        union_llist.append(union_node)
        union_nodes[node.value] = union_node
        ##go to next node in original list
        node = node.next
    
    node = llist_2.head

    while node:
        ##duplicate node in new linked list
        union_node = Node(node.value)
        ##if isnt already in uniojn nodes then add, otherwise skip to next node
        if union_nodes.get(union_node.value,None):
            node = node.next
            continue
        union_llist.append(union_node)
        union_nodes[node.value] = union_node
        ##go to next node in original list
        node = node.next
    
    return union_llist
        

def intersection(llist_1, llist_2):

    llist_1_nodes = {}
    intersection_nodes = {}
    intersection_list = LinkedList()
   
    node = llist_1.head
    while node:     
        llist_1_nodes[node.value] = True
        ##go to next node in original list
        node = node.next
    node = llist_2.head

    while node:
        intersection_node = Node(node.value)

        ##if node is in previous list but not yet added to then add, otherwise skip to next node
        if llist_1_nodes.get(intersection_node.value,None) and not intersection_nodes.get(intersection_node.value, None):
            intersection_list.append(intersection_node)
            intersection_nodes[intersection_node.value] =  intersection_node

        ##go to next node in original list
        node = node.next
    
    return intersection_list      


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))


# Test case 3

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))

# Test case 4

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [1,1,1,1,1,1]
element_2 = [2,2,2,2,2,2,2]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))