from binary_tree import BinaryTree


def line():
    print("=+=" * 20)


def compare_binary_tree_dfs(tree1, tree2):
    # Quando parar?
    if tree1 is None or tree2 is None:
        if tree1 == tree2:
            return True

        return False

    # Quando chamar?
    if tree1.data == tree2.data:
        return compare_binary_tree_dfs(tree1.left, tree2.left) and compare_binary_tree_dfs(tree1.right, tree2.right)

    return False


# Test 1
tree1 = BinaryTree()
tree1.insert(1)
tree1.insert(2)
tree1.insert(3)

tree2 = BinaryTree()
tree2.insert(1)
tree2.insert(2)
tree2.insert(3)

print(compare_binary_tree_dfs(tree1.root, tree2.root))
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

print(compare_binary_tree_dfs(tree1.root, tree2.root))
