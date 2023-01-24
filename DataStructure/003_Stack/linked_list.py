class Node:
    def __init__(self, value):
        self.next = None
        self.value = value


class LinkedList:
    def __init__(self):
        self._head = Node(None)

    def insert_node_to_tail(self, node):
        # elemnt1 -> elemnt2 -> element3 -> None
        self.tail().next = node

    def insert_node_to_head(self, node):
        # elem0 -> novoElemento -> elemento1
        if self._head.next:
            head_element = self._head
            node.next, head_element.next = head_element.next, node
        else:
            self._head.next = node

    def is_empty(self):
        return  self._head.next is None

    def head(self):
        return self._head.next

    def tail(self):
        current = self._head
        while current.next:
            current = current.next

        return current