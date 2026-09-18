my_list = [1, 2, 3, 4]
my_tuple = (1, 2, 3, 4)
my_set = {1, 2, 3, 4}
my_dict = {"name": "Alice", "age": 20}

my_list.pop()
# Tuple items cannot be popped
my_set.pop()
my_dict.pop("age")

print(my_list, my_tuple, my_set, my_dict)