class Node:
    def __init__(self, name: str, id: int | str):
        self.name = name
        self.id = id
        self.next: Node | None = None
