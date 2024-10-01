# Constructing a Linked List
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
linked_list = LinkedList()

# Creating nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

# Linking nodes
node1.next = node2
node2.next = node3

# Setting head
linked_list.head = node1

print(linked_list.head.value)
print(linked_list.head.next.value)
print(linked_list.head.next.next.value)


# Add
new_node = Node(4)
node3.next = new_node
print('Add:')
print(linked_list.head.value)
print(linked_list.head.next.value)
print(linked_list.head.next.next.value)
print(linked_list.head.next.next.next.value)


# Remove
node1.next = node3
print('Remove:')
print(linked_list.head.value)
print(linked_list.head.next.value)
print(linked_list.head.next.next.value)


# Update
node3.value = 10
print('Update:')
print(linked_list.head.value)
print(linked_list.head.next.value)
print(linked_list.head.next.next.value)
