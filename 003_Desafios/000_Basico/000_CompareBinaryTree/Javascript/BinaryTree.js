class Node {
    constructor(data) {
        this.data = data;
        this.left = null;
        this.right = null;
    }
}

class BinaryTree {
    constructor() {
        this.root = null;
    }

    add(data) {
        const node = new Node(data);
        if (this.root === null) {
            this.root = node;
        } else {
            let current = this.root;
            while (current) {
                if (data < current.data) {
                    if (!current.left) {
                        current.left = node;
                        break;
                    }
                    current = current.left;
                } else {
                    if (!current.right) {
                        current.right = node;
                        break;
                    }
                    current = current.right;
                }
            }
        }
    }
}


module.exports = BinaryTree