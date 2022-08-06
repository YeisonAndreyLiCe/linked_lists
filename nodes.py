from queue import Empty


class SLNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class SList:
    def __init__(self):
        self.head = None

    def add_to_front(self, value):
        new_node = SLNode(value)
        current_node = self.head
        new_node.next = current_node
        self.head = new_node
        return self
    
    def print_values(self):
        runner = self.head
        while runner:
            print(runner.value)
            runner = runner.next
        return self

    def add_to_back(self, value):
        if self.head is None:
            self.add_to_front(value)
            return self
        new_node = SLNode(value)
        runner = self.head
        while runner.next:
            runner = runner.next
        runner.next = new_node
        return self
    
    def remove_from_front(self):
        if self.head is None:
            return self
        self.head = self.head.next
        return self

    def remove_from_back(self):
        if self.head is None:
            return self
        if self.head.next is None:
            self.head = None
            return self
        runner = self.head
        while runner.next.next:
            runner = runner.next
        runner.next = None
        return self

    def remove_node(self, value):
        if self.head is None:
            return self
        if self.head.value == value:
            self.head = self.head.next
            return self
        runner = self.head
        while runner.next:
            if runner.next.value == value:
                runner.next = runner.next.next
                return self
            runner = runner.next
        return self

    def insert_node_at(self, value, n=0):
        if n == 0:
            self.add_to_front(value)
            return self
        count = 1
        runner = self.head
        while runner.next:
            if count == n:
                new_node = SLNode(value)
                new_node.next = runner.next
                runner.next = new_node
                return self
            count += 1
            runner = runner.next
        self.add_to_back(value)
        return self
    

        
        

my_list = SList()
my_list.add_to_front("are").add_to_front("hello").add_to_front("Linked lists").add_to_back("fun!").print_values()
print("\n")
my_list.remove_node("hello").print_values()
print("\n")
my_list.insert_node_at('really',2).insert_node_at('Hello').insert_node_at('bye',5).print_values()