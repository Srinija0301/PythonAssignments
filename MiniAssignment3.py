# 1
from collections import Counter
from os import uname
dictionary_one = {'a': 100, 'b': 200, 'c': 300}
dictionary_two = {'a': 300, 'b': 200, 'd': 400}

for key in dictionary_two:
    if key in dictionary_one:
        dictionary_two[key] = dictionary_one[key] + dictionary_two[key]
    else:
        pass
result = {**dictionary_one, **dictionary_two}
print(result)

# 2
original_dictionary = {'c1': 'Red', 'c2': 'Green', 'c3': None}
new_dictionary = {key: value for (key, value) in original_dictionary.items()
                  if value is not None}
print(new_dictionary)

# 3
list1 = [10, 20, 10, 30, 40, 40]
unique_list = []
for x in list1:
    if x not in unique_list:
        unique_list.append(x)
for x in unique_list:
    print(x)


# 4
color1 = ["red", "orange", "green", "blue", "white"]
color2 = ["black", "yellow", "green", "blue"]
for i in color1[:]:
    if i in color2:
        color1.remove(i)
        color2.remove(i)
print("Color1-Color2: ", color1)
print("Color2-Color1: ", color2)

# 5
Sample = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
Sample = [i for i in Sample if i]
print(Sample)

# 6
set = {1, 10, 6, 23, 8, 4}
print(set)
print("Maximum: ", max(set))
print("Minimum: ", min(set))
