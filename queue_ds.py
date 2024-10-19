class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = self.last = new_node
        self.length = 1

    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = self.last = new_node
        else:
            self.last.next = self.last = new_node
        self.length += 1
        return True

    def dequeue(self):
        assert self.length > 0, "self.length must be greater than zero"
        temp = self.first
        if self.length == 1:
            self.first = self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp

    def update(self, index, value):
        assert index >= 0, "index must be greater than or equal to zero"
        assert index < self.length, "index must be less than self.length"
        temp = self.first
        count = 0
        while count < index:
            temp = temp.next
            count += 1
        if temp:
            temp.value = value
            return True
        return False

    def get(self, index):
        assert index >= 0, "index must be greater than or equal to zero"
        assert index < self.length, "index must be less than self.length"
        temp = self.first
        for _ in range(index):
            temp = temp.next
        return temp


# Construct first node of queue
print("Construct first node:")
my_queue = Queue(0)
print(my_queue.first.value)

# Enqueue five more nodes
print("Add:")
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(4)
my_queue.enqueue(5)
print(my_queue.get(0).value)
print(my_queue.get(1).value)
print(my_queue.get(2).value)
print(my_queue.get(3).value)
print(my_queue.get(4).value)
print(my_queue.get(5).value)

# Dequeue first node in queue
print("Remove:")
my_queue.dequeue()
print(my_queue.get(0).value)
print(my_queue.get(1).value)
print(my_queue.get(2).value)
print(my_queue.get(3).value)
print(my_queue.get(4).value)

# Update
print("Update:")
my_queue.update(2, 56)
print(my_queue.get(0).value)
print(my_queue.get(1).value)
print(my_queue.get(2).value)
print(my_queue.get(3).value)
print(my_queue.get(4).value)
