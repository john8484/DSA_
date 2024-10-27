class List:
    def __init__(self):
        self.data = []

    def construct(self, items):
        self.data = []
        for item in items:
            self.data += [item]

    def append(self, item):
        self.data = self.data + [item]

    def remove(self, item):
        new_data = []
        found = False
        for i in self.data:
            if i == item and not found:
                found = True
            else:
                new_data += [i]
        self.data = new_data

    def update(self, index, value):
        assert index >= 0, "index must be greater than or equal to zero"
        assert index < len(self.data), "index must be less than the list's length"
        self.data[index] = value


# Construct the list
my_list = List()
my_list.construct([1, 2, 3, 4, 5])
print("Construct:")
print(my_list.data)

# append an item
my_list.append(6)
print("Add:")
print(my_list.data)

# Remove an item
my_list.remove(3)
print("Remove:")
print(my_list.data)

# Update an item
my_list.update(2, 10)
print("Update:")
print(my_list.data)
