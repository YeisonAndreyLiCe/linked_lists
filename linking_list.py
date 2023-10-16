from node import Node


class LList:
    def __init__(self):
        self.head: Node | None = None

    def insert_node(self, node: Node) -> "LList":
        if self.head is None:
            self.head = node
            return self
        runner = self.head
        while runner.next:
            runner = runner.next
        runner.next = node
        return self

    def insert_nodes(self, nodes: list[Node]) -> "LList":
        for node in nodes:
            self.insert_node(node)
        return self

    def print_values(self) -> "LList":
        aux = self.head
        while aux:
            print(aux.name)
            aux = aux.next
        return self

    def remove_node_at(self, index: int) -> "LList":
        if self.head is None:
            return self
        if index == 0:
            self.head = self.head.next
            return self
        runner = self.head
        while runner.next:
            if index == 1:
                runner.next = runner.next.next
                return self
            runner = runner.next
            index -= 1
        return self
