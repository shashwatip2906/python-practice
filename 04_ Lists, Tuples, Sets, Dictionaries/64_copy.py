my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
my_set = {1, 2, 3}
my_dict = {"a": 1, "b": 2}

list_copy = my_list.copy()
tuple_copy = my_tuple.copy() if hasattr(my_tuple, "copy") else tuple(my_tuple)
set_copy = my_set.copy()
dict_copy = my_dict.copy()

print(list_copy, tuple_copy, set_copy, dict_copy)