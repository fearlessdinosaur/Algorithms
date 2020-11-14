import random as random


class Node:

    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None


def build_offset(offset):
    tab_offset = ""
    for x in range(0, offset):
        tab_offset = tab_offset + "\t"
    return tab_offset


def find_offset(node, offset):
    while node.left is not None:
        offset = offset + 1
        node = node.left
    return offset


class Tree:

    def __init__(self, root):
        self.root = Node(root)

    def append(self, value):
        new_node = Node(value)
        current = self.root
        while current is not None:
            if value > current.value:
                if current.right is not None:
                    current = current.right
                else:
                    current.right = new_node
                    break
            else:
                if current.left is not None:
                    current = current.left
                else:
                    current.left = new_node
                    break

    def traverse(self):
        parent = self.root
        offset = find_offset(parent, 0)
        print("offset:" + str(offset))
        print(build_offset(offset) + str(parent.value))
        if parent.left is not None:
            depth = offset
            self.subtree(parent.left, depth - 1)
        if parent.right is not None:
            depth = offset
            self.subtree(parent.right, depth + 1)

    def subtree(self, current, depth):

        if current is not None:
            tabs = ""
            print(build_offset(depth) + str(current.value))
        else:
            print("None")

        if current.left is None:
            if current.right is None:
                return 0
            else:
                self.subtree(current.right, depth + 1)

        else:
            self.subtree(current.left, depth - 1)


def main():
    sample_tree = Tree(random.randint(0, 50))
    for x in range(0, 10):
        sample_tree.append(random.randint(0, 50))
    sample_tree.traverse()


if __name__ == '__main__':
    main()
