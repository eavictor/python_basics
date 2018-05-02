class Node(object):
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None


def insert_binary_node(root, node):
    if root is None:
        root = node

    else:
        if node.value > root.value:
            if root.right_child is None:
                root.right_child = node
            else:
                insert_binary_node(root.right_child, node)
        else:
            if root.left_child is None:
                root.left_child = node
            else:
                insert_binary_node(root.left_child, node)


# print order: left_child, self, right_child
def in_order_print(node):
    if not node:
        return

    in_order_print(node.left_child)

    print(node.value)

    in_order_print(node.right_child)


# print order: self, left_child, right_child
def pre_order_print(node):
    if not node:
        return

    print(node.value)
    pre_order_print(node.left_child)
    pre_order_print(node.right_child)


# print order: left_child, right_child, self
def post_order_print(node):
    if not node:
        return

    post_order_print(node.left_child)
    post_order_print(node.right_child)
    print(node.value)


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)  # insert at position 0, all elements behind will shift 1 and "len" will also +1

    def dequeue(self):
        return self.items.pop()  # remove last element

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[self.size() - 1]


def breadth_first_traversal(root):
    if root is None:
        return []

    visited = set([])
    q = Queue()
    q.enqueue(root)
    list_leaves = []

    while not q.is_empty():
        root = q.dequeue()
        print('Current node value:', root.value, q.size())
        visited.add(root)
        left_child = root.left_child

        if left_child is not None and left_child not in visited:
            q.enqueue(left_child)

        right_child = root.right_child
        if right_child is not None and right_child not in visited:
            q.enqueue(right_child)

        list_leaves.append(root.value)
    return list_leaves


def search_value(root, value):
    if value == root.value:
        return True

    elif value < root.value:
        if root.left_child is None:
            return False
        else:
            return search_value(root.left_child, value)

    elif value > root.value:
        if root.right_child is None:
            return False
        else:
            return search_value(root.right_child, value)


def main():
    nums = [50, 25, 100, 57, 68, 1, 4, 39]
    root = Node(nums[0])

    for index, num in enumerate(nums):
        if index == 0:
            continue
        else:
            insert_binary_node(root, Node(num))

    print('In Order Print')
    in_order_print(root)
    print('')

    print('Pre Order Print')
    pre_order_print(root)
    print('')

    print('Post Order Print')
    post_order_print(root)
    print('')

    print('Level Order Print (BFS)')
    print(breadth_first_traversal(root), '\n')

    print('Search Value')
    print(search_value(root, nums[-1]))


if __name__ == '__main__':
    main()
