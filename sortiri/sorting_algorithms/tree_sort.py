from support.binary_tree import Node


def store_sorted(root, sequence, current_index):
    """Linearise the binary search tree into an array of sorted numbers."""
    if root != None:
        current_index = store_sorted(root.left, sequence, current_index)
        sequence[current_index] = root.key
        current_index = current_index + 1
        current_index = store_sorted(root.right, sequence, current_index)
    
    return current_index


def insert(node, key):
    """Insert a given key into the binary search tree."""
    # if the tree is empty, return a new node
    if node == None:
        return Node(key)

    # recurse down the tree
    if key < node.key:
        node.left  = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)
 
    return node


def tree_sort(sequence):
    """Perform tree sort on a sequence of numbers."""
    root = Node(sequence[0])
 
    # construct search tree
    for value in sequence[1:]:
        insert(root, value)
 
    # linearise the search tree into a sorted sequence
    store_sorted(root, sequence, 0)

    return sequence
