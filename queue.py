# Constructing a Queue
class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None  
class Queue:
    def __init__(self):
        self.front = None  
        self.rear = None   
queue = Queue()

first_node = Node(1)
queue.front = first_node  
queue.rear = first_node   

second_node = Node(2)
queue.rear.next = second_node  
queue.rear = second_node  

print(queue.front.data)
print(queue.rear.data)


# Add
third_node = Node(3)
queue.rear.next = third_node  
queue.rear = third_node       
print('Add:')
print(queue.front.data)
print(queue.front.next.data)
print(queue.rear.data)


# Remove
queue.front = queue.front.next
print('Remove:')
print(queue.front.data)
print(queue.rear.data)


# Update
queue.front.data = 17
print('Update:')
print(queue.front.data)
print(queue.rear.data)
