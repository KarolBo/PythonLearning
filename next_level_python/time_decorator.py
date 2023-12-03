from typing import Callable, ParamSpec, Concatenate, TypeVar
import time

Param = ParamSpec("Param")
RetType = TypeVar("RetType")
OriginalFunc = Callable[Param, RetType]
DecoratedFunc = Callable[Concatenate[str, Param], RetType]

def measure_time() -> Callable[[OriginalFunc], DecoratedFunc]:
    def decorator(func: OriginalFunc) -> DecoratedFunc:
        def wrapper(*args, **kwargs) -> RetType:
            start: float = time.time()
            result: RetType = func(*args, **kwargs) 
            stop: float = time.time()
            print(f'{__name__} executed in {stop - start} s')
            return result

        return wrapper

    return decorator


if __name__ == '__main__':
    @measure_time
    def test_time():
        time.sleep(5)

    test_time()