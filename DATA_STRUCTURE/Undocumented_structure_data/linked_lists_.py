# Добавление в начало по скорости превосходит списки
class Node:
    def __init__(self, value=None):
        self.data_value = value
        self.next_value = None

class SingleLinkedList:
    def __init__(self):
        self.head_value = None

    def inser_at_start(self, new_data):
        new_node = Node(new_data)
        new_node.next_value = self.head_value
        self.head_value = new_node

    def insert_at_end(self, new_data):
        new_node = Node(new_data)
        if self.head_value is None:
            self.head_value = new_node
            return
        last = self.head_value
        while last.next_value:
            last = last.next_value
        last.next_value = new_node

    def print_list(self):
        value_to_print = self.head_value
        while value_to_print is not None:
            print(value_to_print.data)
            value_to_print = value_to_print.next_value

class LLInterface:
    def __init__(self):
        self.linked_list = SingleLinkedList()

    def convert(self, iterable):
        self.linked_list.head_value = Node(iterable[0])
        nodes = [Node(value) for value in iterable]
        for index, node in enumerate(nodes):
            if index == 0:
                self.linked_list.head_value = node
            if index < len(nodes) - 1:
                node.next_value = nodes[index + 1]

    def print(self):
        self.linked_list.print_list()

    def add_left(self, value):
        self.linked_list.inser_at_start(value)
    def add_right(self, value):
        self.linked_list.insert_at_end(value)


ll_interface = LLInterface()
ll_interface.convert([1, 2, 3, 4])
ll_interface.add_left(0)
ll_interface.add_right(5)