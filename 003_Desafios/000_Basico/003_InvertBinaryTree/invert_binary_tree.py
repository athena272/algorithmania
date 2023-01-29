from binary_tree import BinaryTree, print_tree

def line():
    print("=+=" * 20)


def invert_binary_tree(tree):
    # Quando parar?
    if tree.left is None and tree.right is None:
        return tree

    # O que repetir?
    # Inverter valores
    tree.left, tree.right = tree.right, tree.left
    # Verifcar se existem filhos
    if tree.left:
        tree.left = invert_binary_tree(tree.left)

    if tree.right:
        tree.right = invert_binary_tree(tree.right)

    return tree


# Test 1
tree = BinaryTree()
tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)
tree.insert(6)
tree.insert(7)
tree.insert(8)

print_tree(tree.root)
line()

invert_binary_tree(tree.root)
print_tree(tree.root)
