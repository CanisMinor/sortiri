from queue import Queue
from sets import Set

def breadth_first_search(root):
    nodes = Queue()
    visited_nodes = Set()
    nodes.enqueue(root)
  
    while not nodes.is_empty():
        subtree_root = nodes.dequeue()
        for child in nodes.children:
            if child not in visited_nodes:
                nodes.enqueue(child)
    
        visited_nodes.add(subtree_root)
