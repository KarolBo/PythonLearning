from typing import Generator


# Generator[YieldType, SendType, ReturnType]
def echo_round() -> Generator[int, float, str]:
    sent = yield 0
    while sent >= 0:
        sent = yield round(sent)
    return 'Done'

echo = echo_round()
print(next(echo))
print(echo.send(1.6))
print(echo.send(1.2))
print(echo.send(1.9))
try:
    print(echo.send(-0.1))
except StopIteration as err:
    print(err)
