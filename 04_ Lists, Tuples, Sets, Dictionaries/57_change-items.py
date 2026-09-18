my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_set = {1, 2, 3, 4, 5}
my_dict = {"name": "Alice", "age": 20}

my_list[0] = 10
# Tuple items cannot be changed directly
my_set.remove(1); my_set.add(10)
my_dict["name"] = "Bob"

print(my_list, my_tuple, my_set, my_dict)