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


# Construct first node of linked list
linked_list = LinkedList(1)
print("Construct first node:")
print(linked_list.head.value)

# Add five more nodes
linked_list.prepend(2)
linked_list.prepend(3)
linked_list.prepend(4)
linked_list.prepend(5)
linked_list.prepend(6)
print("Add:")
print(linked_list.head.value)
print(linked_list.head.next.value)
print(linked_list.head.next.next.value)
print(linked_list.head.next.next.next.value)
print(linked_list.head.next.next.next.next.value)
print(linked_list.head.next.next.next.next.next.value)

# Remove last node
linked_list.pop()
print("Remove:")
print(linked_list.head.value)
print(linked_list.head.next.value)
print(linked_list.head.next.next.value)
print(linked_list.head.next.next.next.value)
print(linked_list.head.next.next.next.next.value)

# Update
linked_list.update(2, 56)
print("Update:")
print(linked_list.head.value)
print(linked_list.head.next.value)
print(linked_list.head.next.next.value)
print(linked_list.head.next.next.next.value)
print(linked_list.head.next.next.next.next.value)
