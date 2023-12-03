from typing import Iterator

my_list: list[int] = [1, 2, 3, 4, 5, 6, 7]

# my_iter: Iterator[int] = my_list.__iter__()
my_iter: Iterator[int] = iter(my_list)

print(my_iter.__next__())
print(next(my_iter))
print()
for val in my_iter:
    print(val)
try:
    print(next(my_iter))
except StopIteration:
    print('no more elements')


print()
with open('numbers.txt') as file:
    file_iter = iter(file.readline, "")
    for line in file_iter:
        print(line, end="") # sentinel
print()