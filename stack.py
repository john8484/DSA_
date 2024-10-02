# Constructing a Stack
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class Stack:
    def __init__(self):
        self.top = None


stack = Stack()
new_node = Node(1)
stack.top = new_node

new_node = Node(2)
new_node.next = stack.top
stack.top = new_node

new_node = Node(3)
new_node.next = stack.top
stack.top = new_node

print(stack.top.value)
print(stack.top.next.value)
print(stack.top.next.next.value)


# Add
new_node = Node(4)
new_node.next = stack.top
stack.top = new_node
print('Add:')
print(stack.top.value)
print(stack.top.next.value)
print(stack.top.next.next.value)
print(stack.top.next.next.next.value)


# Remove
stack.top = stack.top.next
print('Remove:')
print(stack.top.value)
print(stack.top.next.value)
print(stack.top.next.next.value)


# Update
stack.top.value = 91
print('Update:')
print(stack.top.value)
print(stack.top.next.value)
print(stack.top.next.next.value)
