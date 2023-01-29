from binary_tree import BinaryTree
from breadth_first_search import breadth_first_search


def minimum_deep(root):
    if root:
        queue = [(root, 0)]
        while queue:
            node, level = queue.pop(0)

            if node.left is None and node.right is None:
                return level

            level += 1
            if node.left:
                queue.append((node.left, level))

            if node.right:
                queue.append((node.right, level))

    return 0


    # Test 1
tree = BinaryTree()
tree.insert(3)
tree.insert(9)
tree.insert(15)
tree.insert(7)

print(minimum_deep(tree.root))
