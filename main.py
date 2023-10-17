
class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, data):
        self.children.append(data)

class Tree:
    def __init__(self, root_data):
        self.root = Node(root_data)


tree = Tree("Root")
child1 = Node("Child 1")
child2 = Node("Child 2")
child3 = Node("Child 3")

child1.add_child("Child 1.1")
child1.add_child("Child 1.2")
child1.add_child("Child 1.3")

child3.add_child("Child 3.1")
child3.add_child("Child 3.2")
child3.add_child("Child 3.3")

tree.root.add_child(child1)
tree.root.add_child(child2)
tree.root.add_child(child3)


def dfs(path, deeply_list=None):
    if deeply_list is None:
        deeply_list = [path.data]
    for i in path.children:
        if isinstance(i, Node):
            deeply_list.append(i.data)
            dfs(i, deeply_list)
        else:
            deeply_list.append(i)

    return deeply_list


print(dfs(tree.root))
