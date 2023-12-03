from typing import Generator


# Generator expression
generator = (x**2 for x in range(20))
for pow in generator:
    print(pow)

    

def normal_generator() -> Generator[int, None, None]:
    i = 0
    while i < 10:
        i += 1
        yield i-1

gen = normal_generator()
for i in gen:
    print(i)

