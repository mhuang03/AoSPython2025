class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class List:
    def __init__(self, *values):
        if len(values) == 0:
            raise RuntimeError("Must pass at least one value")

        self.head = Node(values[0])
        current = self.head
        for value in values[1:]:
            new_node = Node(value, current)
            current.next = new_node
            current = new_node
        self.tail = current

    def print_forward(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

    def print_backward(self):
        current = self.tail
        while current is not None:
            print(current.value)
            current = current.prev


l1 = List(1, 2, 3, 4 ,5)
l1.print_forward()
l1.print_backward()