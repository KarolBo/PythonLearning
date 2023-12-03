from functools import cached_property, singledispatch
from statistics import stdev


class Data:
    def __init__(self):
        self.numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    @cached_property
    def std(self) -> float:
        print('Calculating STD...')
        return stdev(self.numbers)
    

################################################
    

@singledispatch
def handle(x: int) -> str:
    return f'I am Integer: {x}'

@handle.register
def _(x: str) -> str:
    return f'I am String: {x}'

handle.register(list, lambda x: f'I am List: {[*x[2:], *x[:2]]}')
    
    
if __name__ == '__main__':
    data = Data()
    print(data.std)
    print(data.std)
    print(data.std)
    data.numbers = [5, 10, 15, 25]
    print(data.std)
    print(data.std)

    print()
    print(handle(5))
    print(handle('dupa'))
    print(handle([1, 2, 3, 4, 5, 6]))
    print(handle(1.5))