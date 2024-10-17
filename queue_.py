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
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp

    def update(self, index, value):
        if index < 0 or index >= self.length:
            return None
        temp = self.first
        count = 0
        while count < index:
            temp = temp.next
            count += 1
        if temp:
            temp.value = value
            return True
        return False


# Construct first node of queue
my_queue = Queue(1)
print("Construct first node:")
print(my_queue.first.value)

# Add five more nodes
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(4)
my_queue.enqueue(5)
my_queue.enqueue(6)
print("Add:")
print(my_queue.first.value)
print(my_queue.first.next.value)
print(my_queue.first.next.next.value)
print(my_queue.first.next.next.next.value)
print(my_queue.first.next.next.next.next.value)
print(my_queue.first.next.next.next.next.next.value)

# Remove first node in queue
my_queue.dequeue()
print("Remove:")
print(my_queue.first.value)
print(my_queue.first.next.value)
print(my_queue.first.next.next.value)
print(my_queue.first.next.next.next.value)
print(my_queue.first.next.next.next.next.value)

# Update
my_queue.update(2, 56)
print("Update:")
print(my_queue.first.value)
print(my_queue.first.next.value)
print(my_queue.first.next.next.value)
print(my_queue.first.next.next.next.value)
print(my_queue.first.next.next.next.next.value)
