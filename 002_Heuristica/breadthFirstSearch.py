class Node:
    value: 0
    left = None
    right = None


def breadthFirstSearch(root, valueToFind):
    if root:
        queue = [root]
        while queue:
            node = queue.pop(0)

            # Checa se é o nó que esperamos
            if node.value == valueToFind:
                return True

            # Analisar os filhos
            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)
