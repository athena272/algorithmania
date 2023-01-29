const BinaryTree = require('./BinaryTree')

function line() {
    console.log('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
}

function compareBinaryTreeDFS(tree1, tree2) {
    // Quando parar?
    if (tree1 == null || tree2 == null) {
        if (tree1 == tree2) {
            return true
        }
        return false
    }

    // Quando chamar?
    if (tree1.data == tree2.data) {
        return compareBinaryTreeDFS(tree1.left, tree2.left) && compareBinaryTreeDFS(tree1.right, tree2.right)
    }

    return false
}

// Test 1
tree1 = new BinaryTree()
tree1.add(1)
tree1.add(2)
tree1.add(3)

tree2 = new BinaryTree()
tree2.add(1)
tree2.add(2)
tree2.add(3)

console.log(compareBinaryTreeDFS(tree1.root, tree2.root))
line()

// Test 2
tree1 = new BinaryTree()
tree1.add(1)
tree1.add(2)
tree1.add(3)

tree2 = new BinaryTree()
tree2.add(1)
tree2.add(2)
tree2.add(4)
tree2.add(5)
tree2.add(3)

console.log(compareBinaryTreeDFS(tree1.root, tree2.root))
