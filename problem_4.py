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

class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

class Group_State(object):
    def __init__(self,node):
        self.node = node
        ##copy node.groups list
        self.unvisited_child_groups = node.groups[:]
        self.visited_child_groups = []
        
    def get_node(self):
        return self.node
    
    def visit_child_group(self):
        if self.unvisited_child_groups:
            visited_group =  self.unvisited_child_groups.pop()
            self.visited_child_groups.append(visited_group)
            return visited_group
        return None
    
    def get_visited_child_groups(self):
        return self.visited_child_groups

    def get_unvisited_child_groups(self):
        return self.unvisited_child_groups
    
        
    def __repr__(self):
        s = f"""{self.node}
visited_left: {self.visited_left}
visited_right: {self.visited_right}
        """
        return s



def user_is_in_current_group(user, current_group):
    group_users = current_group.get_users()

    return user in group_users



def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    stack = Stack()
  
    group_state = Group_State(group)
    stack.push(group_state)

    while group:

        ##first check if user in current group
        if user_is_in_current_group(user, group_state.get_node()):
            return True

        if group_state.get_unvisited_child_groups():
            ##visit next child
            group = group_state.visit_child_group()
            group_state = Group_State(group)
            stack.push(group_state)
        ##otherwise visited all children so pop off stack
        else:
            stack.pop()
            group_state = stack.top()
            group = group_state.get_node() if group_state else None

        
    return False

####################################################################################################

################################ TESTS #############################################################


##test user_is_in_current_group
group = Group("my_group")
[group.add_user(f"User {i}") for i in range(10)]
test("should return true if user in group", True,user_is_in_current_group("User 5", group) ==True )
test("should return false if user not in group", True, user_is_in_current_group("User 92", group) ==False )


## test main function
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

parent_user = "parent_user"
child_user = "child_user"

parent.add_user(parent_user)
child.add_user(child_user)

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

test("should return true if user in sub_child group", True, is_user_in_group(sub_child_user, sub_child) ==True )
test("should return true if user in child group", True, is_user_in_group(child_user, child) ==True )
test("should return true if user in parent group", True, is_user_in_group(child_user, child) ==True )
test("should return false if user not in sub_child group", True, is_user_in_group("non_existent_user", sub_child) ==False )
test("should return true if user in child group", True, is_user_in_group("non_existent_user", child) ==False )
test("should return true if user in parent group", True, is_user_in_group("non_existent_user", child) ==False )

parent = Group("parent")
test("should return false for empty parent group", True, is_user_in_group("non_existent_user", parent)==False)