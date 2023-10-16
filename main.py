from node import Node
from linking_list import LList


if __name__ == "__main__":
    persons = [("John", 1), ("Mary", 2), ("Bob", 3), ("Jane", 4), ("Joe", 5)]
    nodes = [Node(name, id) for name, id in persons]

    linked_list = LList()
    linked_list.insert_nodes(nodes)
    linked_list.print_values()
