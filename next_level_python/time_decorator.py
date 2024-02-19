from typing import Callable, ParamSpec, Concatenate, TypeVar
import time

Param = ParamSpec("Param")
RetType = TypeVar("RetType")
OriginalFunc = Callable[Param, RetType]
DecoratedFunc = Callable[Concatenate[str, Param], RetType]

# def measure_time() -> Callable[[OriginalFunc], DecoratedFunc]:

def measure_time(unit: str) -> DecoratedFunc:
    def decorator(func: OriginalFunc):
        def wraper(*args, **kwargs) -> RetType:
            start: float = time.time()
            result: RetType = func(*args, **kwargs) 
            stop: float = time.time()
            if unit == 'ms':
                start *= 1000
                stop *= 1000
            print(f'{__name__} executed in {stop - start} {unit}')
            return result

        return wraper
    return decorator

# return measure_time


if __name__ == '__main__':
    @measure_time('ms')
    def test_time(delay):
        time.sleep(delay)

    test_time(3)