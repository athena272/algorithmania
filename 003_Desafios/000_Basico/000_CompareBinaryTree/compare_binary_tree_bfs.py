from binary_tree import BinaryTree


def line():
    print("=+=" * 20)


def compare_binary_tree_bfs(tree1, tree2):
    queue = [(tree1, tree2)]

    while queue:
        t1, t2 = queue.pop(0)

        if t1 is None or t2 is None:
            if t1 == t2:
                continue

            return False

        if t1.data != t2.data:
            return False

        queue.append((t1.left, t2.left))
        queue.append((t1.right, t2.right))

    return True


# Test 1
tree1 = BinaryTree()
tree1.insert(1)
tree1.insert(2)
tree1.insert(3)

tree2 = BinaryTree()
tree2.insert(1)
tree2.insert(2)
tree2.insert(3)

print(compare_binary_tree_bfs(tree1.root, tree2.root))
line()

# Test 2
tree1 = BinaryTree()
tree1.insert(1)
tree1.insert(2)
tree1.insert(3)

tree2 = BinaryTree()
tree2.insert(1)
tree2.insert(2)
tree2.insert(4)
tree2.insert(5)
tree2.insert(3)

print(compare_binary_tree_bfs(tree1.root, tree2.root))
