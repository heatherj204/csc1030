import random, time

class Node:

    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __repr__(self):
        return f"{self.data}"

class DoublyLinkedList:

    def __init__(self):
        self._size = 0
        self.head = None
        self.tail = None

    def add_first(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self._size += 1

    def remove_first(self):
        if not self.head:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self._size -= 1

    def add_last(self, data):
        new_node = Node(data)
        if not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self._size += 1

    def remove_last(self):
        if not self.tail:
            return
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self._size -= 1

    def first(self):
        return self.head

    def last(self):
        return self.head

    def __len__(self):
        return self._size

    def insert_before(self, node, data):
        new_node = Node(data)
        if node.prev:
            node.prev.next = new_node
            new_node.prev = node.prev
        else:
            self.head = new_node

        new_node.next = node
        node.prev = new_node

        self._size += 1

    def insert_after(self, node, data):
        new_node = Node(data)
        if node.next:
            new_node.prev = node
            new_node.next = node.next
            node.next.prev = new_node
            node.next = new_node
        else:
            node.next = new_node
            new_node.prev = node
            self.tail = new_node
        self._size += 1

    def add_sorted(self, data):

        if not self.head:
            new_node = Node(data)
            self.head = new_node
            self.tail = new_node
            self._size += 1
        else:
            current = self.head
            while current and current.data < data:
                current = current.next
            if not current:
                self.add_last(data)
            else:
                self.insert_before(current, data)

    def display(self):
        current = self.head
        while current:
            print(str(current.data), end=" --> ")
            current = current.next
        print(None)


if __name__ == '__main__':

    linked_list = DoublyLinkedList()

    linked_list.add_last("A")
    linked_list.add_last("B")
    linked_list.add_last("C")

    linked_list.display()

    random_list = [random.randint(0, 100000) for _ in range(20000)]

    print("Start Simulation")

    # Maintaining a sorted list using a Doubly Linked List
    # O(n) to find the position and O(1) for the insert
    sorted_list = DoublyLinkedList()
    start_time = time.time()
    for val in random_list:
        sorted_list.add_sorted(val)
    print(f"Linked List insert time: {time.time() - start_time}")

    # Maintaining a sorted list using a standard list
    # O(n) to find the position and O(n) for the insert (note that it is linear time for both operations)
    std_sorted_list = []
    start_time = time.time()
    for value in random_list:
        index = 0
        while index < len(std_sorted_list) and std_sorted_list[index] < value:
            index += 1
        std_sorted_list.insert(index, value)
    print(f"Standard List insert time: {time.time() - start_time}")

    print("End Simulation")








