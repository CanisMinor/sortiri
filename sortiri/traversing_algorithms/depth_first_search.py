from stack import Stack

def depth_first_search(root):
    nodes = Stack()
    nodes.append(root)

    while not nodes.empty():
        current_node = nodes.pop()
        for child in current_node.children:
            nodes.append(child)
