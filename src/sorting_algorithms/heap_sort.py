def heapify(sequence, heap_size, root):
    largest = root
    left = (2 * root) + 1
    right = (2 * root) + 2

    # See if left child of root exists and is greater than root
    if left < heap_size and sequence[root] < sequence[left]:
        largest = left

    # See if right child of root exists and is greater than root
    if right < heap_size and sequence[largest] < sequence[right]:
        largest = right

    # Change root, if needed
    if largest != root:
        sequence[root], sequence[largest] = sequence[largest], sequence[root]

        # Heapify the root.
        heapify(sequence, heap_size, largest)

def heap_sort(sequence):
    num_entries = len(sequence)

    # Build a maxheap.
    for i in range(num_entries, -1, -1):
        heapify(sequence, num_entries, i)

    # One by one extract elements
    for i in range(num_entries - 1, 0, -1):
        sequence[i], sequence[0] = sequence[0], sequence[i]
        heapify(sequence, i, 0)
