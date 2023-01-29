const BinaryTree = require('./BinaryTree')

function line() {
    console.log('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
}

function isArrayOnlyNull(arr) {
    return arr.every(element => element === null);
}

function compareBinaryTreeBFS(tree1, tree2) {
    const queue = [(tree1, tree2)]

    while (!isArrayOnlyNull(queue)) {
        const t1 = queue.pop(0)
        const t2 = t1

        if (t1 === null || t2 === null) {
            if (t1 === t2) {
                continue
            }
            return false
        }
        if (t1.data !== t2.data) {
            return false
        }

        queue.push((t1.left, t2.left))
        queue.push((t1.right, t2.right))
    }
    return true
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

console.log(compareBinaryTreeBFS(tree1.root, tree2.root))
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

console.log(compareBinaryTreeBFS(tree1.root, tree2.root))