import os

##simple test helper function
def test(msg,expectation, comparison):
    if expectation == comparison:
        return print(f"{msg}: Passed")
    return print(f"{msg}: Failed")


class Stack():
    def __init__(self):
        self.list = list()
        
    def push(self,value):
        self.list.append(value)
        
    def pop(self):
        return self.list.pop()
        
    def top(self):
        if len(self.list) > 0:
            return self.list[-1]
        else:
            return None
        
    def is_empty(self):
        return len(self.list) == 0
    
    def __repr__(self):
        if len(self.list) > 0:
            s = "<top of stack>\n_________________\n"
            s += "\n_________________\n".join([str(item) for item in self.list[::-1]])
            s += "\n_________________\n<bottom of stack>"
            return s
        
        else:
            return "<stack is empty>"

##state object to keep track of if node has been visisted and which of its children have been visited
class State():
  def __init__(self, path):
    self.path = path
    self.children = []
    self.visited = False
     
  ##child paths are relative to parent
  def set_children(self):
    if os.path.isdir(self.path):
      self.children =  os.listdir(self.path)
   
  def visit_child(self):
    if self.get_child_count():
      return self.children.pop()
    return None

  def get_child_count(self):
    return len(self.children)
    
  def is_file(self):
    return os.path.isfile(self.path)


##helper function to format file paths correctly
def get_formatted_path(path):
  ##if folder add / to front of string
  if os.path.isfile(path):
    return path
  return path + "/"

##helper function to match file path
def contains_suffix(path, suffix):
  import re
  ##use regex to match suffix in path
  return bool(re.search(rf"\{suffix}$",rf"{path}"))

##tree navigation excercise
def find_files(suffix, path):

    order_visited = []
    order_visited_with_suffix = []
    root = State(path)
    stack = Stack()
    node = root  
    loop_count = 0

    while node:
      loop_count +=1
      ##only get children, push node to stack etc. if node is yet to be visited
      if not node.visited:
        ##check children
        node.set_children()
        ##add to stack
        stack.push(node)
        order_visited.append(node.path)

        ##if current node is a file and it contains suffix, add to suffix array
        if (contains_suffix(node.path, suffix) and node.is_file()):
          order_visited_with_suffix.append(node.path)

        node.visited = True

      ##in all cases, get next child if exists
      if node.get_child_count():
        ##if parent has children it must have "/" at end so we can get the correct paths for the children relative to base folder
        formatted_parent_path = get_formatted_path(node.path)
        joined_path = os.path.join(formatted_parent_path, node.children[-1])
        ##remove node from child array as we are about to visit it
        node.visit_child()
        ##update current node and traverse into next level of tree
        node = State(joined_path)
        continue
      
      ##else there are no children, or already visited them all
      ##so pop current element off the stack
      elif not stack.is_empty():
        stack.pop()

      ##if stack empty this will be none and loop ends
      node = stack.top()
  
    return (order_visited, order_visited_with_suffix)


############################# TESTS #############################################
##test the custom state class    
testState = State('./testdir2')
testState.set_children()
[testState.visit_child() for i in range(4)]
test("get_child_count should return false once all children popped from array", True,testState.get_child_count() == 0)

##test get_formatted_path function works
test("Should leave input unchange if file", True, get_formatted_path("./testdir2/file.txt") == "./testdir2/file.txt")
test("Should add / to end if directory", True, get_formatted_path("./testdir2") == "./testdir2/")

##test contains_suffix function works
test("should return True if suffix found", True, contains_suffix("myfile.c", ".c") == True)
test("should return False if suffix present but not at end of string", True, contains_suffix("dir1.c.mydir", ".c") == False)
test("should return False if suffix not found", True, contains_suffix("myfile", ".c") == False)

##test traverses tree correctly
test("Should visit the correct number of files/folders",True, len(find_files(".c", './testdir2')[0]) == 6)
test("Should visit the correct number of files/folders",True, len(find_files(".c", './testdir3')[0]) == 1)

#final complete tests
test("Should return all files which match the suffix", True, len(find_files(".c","./testdir")[1]) == 4)
print(find_files(".c","./testdir")[1]) ##should return ['./testdir/t1.c', './testdir/subdir5/a.c', './testdir/subdir3/subsubdir1/b.c', './testdir/subdir1/a.c']
test("Should not return any files if none match", True, len(find_files(".c","./testdir2")[1]) == 0)
test("Should return all files which match the suffix even if some folernames include the suffix", True, len(find_files(".c","./testdir5")[1]) == 2)
test("Should return empty array if folder empty", True, len(find_files(".c","./emptydir")[1]) == 0)


print(find_files(".c","./testdir")[1])
##print("order visited",find_files("",'./testdir2'))
