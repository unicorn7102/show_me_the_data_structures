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


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    
    usrs = group.get_users()
    grps = group.get_groups()
    
    if user in usrs: return True
    
    for grp in grps:
        if(is_user_in_group(user, grp)): return True
        
    return False

if __name__ == '__main__':
    
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    parent_user = "parent_user"
    parent.add_user(parent_user)

    child_user = "child_user"
    child.add_user(child_user)

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    print(is_user_in_group(parent_user, parent))
    print(is_user_in_group(parent_user, child))
    print(is_user_in_group(parent_user, sub_child))
    # True, False, False

    print(is_user_in_group(child_user, parent))
    print(is_user_in_group(child_user, child))
    print(is_user_in_group(child_user, sub_child))
    # True, True, False

    print(is_user_in_group(sub_child_user, parent))
    print(is_user_in_group(sub_child_user, child))
    print(is_user_in_group(sub_child_user, sub_child))
    # True, True, True