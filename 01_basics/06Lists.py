fruits = ["apple", "banana", "cherry", "orange", "blueberry"]
for i in range(len(fruits)):
    remaining_fruits = fruits[i:]
    print(remaining_fruits)
print([])

# List append .Takes one argument
fruits = ["orange", "apple", "pear", "banana", "kiwi", "apple", "banana"]
fruits.append("patates")
print(fruits)

# List extend . Multi items
fruits.extend(["karpuz", "Muz", "Kavun"])
print(fruits)

tools = ["pen", "hammer", "lever"]
tools_slice = tools[1:3]  # ['hammer', 'lever']
tools_slice[0] = "nail"

# Original list is unaltered:
print(tools_slice)  # ['nail', 'lever']
