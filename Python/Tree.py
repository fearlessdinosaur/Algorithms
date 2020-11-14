import random as random


class Node:

    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None


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
                    print("stepping down one node to:"+str(current.value))
                else:
                    current.right = new_node
                    break
            else:
                if current.left is not None:
                    current = current.left
                    print("stepping down one node to:"+str(current.value))
                else:
                    current.left = new_node
                    break

    def traverse(self):
        parent = self.root
        print(parent.value)
        if parent.left is not None:
            depth = 1
            self.subtree(parent.left, depth)
        if parent.right is not None:
            depth = 1
            self.subtree(parent.right, depth)

    def subtree(self, current, depth):

        if current is not None:
            tabs = ""
            for x in range(0, depth):
                tabs = tabs + "\t"
            print(tabs + str(current.value))
        else:
            print("None")

        if current.left is None:
            if current.right is None:
                return 0
            else:
                self.subtree(current.right, depth + 1)

        else:
            self.subtree(current.left, depth + 1)


def main():
    sample_tree = Tree(5)
    for x in range(0, 10):
        sample_tree.append(random.randint(0, 50))
    sample_tree.traverse()


if __name__ == '__main__':
    main()
