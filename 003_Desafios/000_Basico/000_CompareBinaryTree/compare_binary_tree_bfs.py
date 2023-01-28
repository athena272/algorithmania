from binary_tree import BinaryTree


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

        queue.append(t1.left, t2.left)
        queue.append(t1.right, t2.right)


    return True
