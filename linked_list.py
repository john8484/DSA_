class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = self.tail = new_node
        self.length = 1

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = self.tail = new_node
        else:
            self.tail.next = self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.head = self.tail = None
        return temp

    def update(self, index, value):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        count = 0
        while count < index:
            temp = temp.next
            count += 1
        if temp:
            temp.value = value
            return True
        return False

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp


# Construct first node of linked list
linked_list = LinkedList(0)
print("Construct first node:")
print(linked_list.get(0).value)

# Add five more nodes
linked_list.prepend(1)
linked_list.prepend(2)
linked_list.prepend(3)
linked_list.prepend(4)
linked_list.prepend(5)
print("Add:")
print(linked_list.get(0).value)
print(linked_list.get(1).value)
print(linked_list.get(2).value)
print(linked_list.get(3).value)
print(linked_list.get(4).value)
print(linked_list.get(5).value)

# Remove first node
linked_list.pop()
print("Remove:")
print(linked_list.get(0).value)
print(linked_list.get(1).value)
print(linked_list.get(2).value)
print(linked_list.get(3).value)
print(linked_list.get(4).value)

# Update
linked_list.update(2, 56)
print("Update:")
print(linked_list.get(0).value)
print(linked_list.get(1).value)
print(linked_list.get(2).value)
print(linked_list.get(3).value)
print(linked_list.get(4).value)
