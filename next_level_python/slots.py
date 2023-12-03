from dataclasses import dataclass
from timeit import repeat
from statistics import median
from functools import partial


@dataclass(slots=False)
class FooDict:
    value: str


@dataclass(slots=True)
class FooSlots:
    value: str

class FooSlotsDirect:
    __slots__ = ('value',)

    def __init__(self, value):
        self.value = value


def get_set_delete(value_object: FooDict | FooSlots | FooSlotsDirect):
    value_object.value = 'dupa123'
    value_object.value
    del value_object.value

if __name__ == '__main__':
    foo_dict = FooDict('test_value')
    foo_slots = FooSlots('test_value')
    foo_slots_direct = FooSlotsDirect('test_value')

    median_time_dict = median(repeat(partial(get_set_delete, foo_dict), number=100000))
    median_time_slots = median(repeat(partial(get_set_delete, foo_slots), number=100000))
    median_time_slots_direct = median(repeat(partial(get_set_delete, foo_slots_direct), number=100000))

    print(f'Dict: {median_time_dict * 1000} ms')
    print(f'Slots: {median_time_slots * 1000} ms')
    print(f'Slots (direct): {median_time_slots_direct * 1000} ms')
    print(f'Performance improvement: {median_time_slots / median_time_dict * 100} %')
    print(f'Performance improvement (direct): {median_time_slots_direct / median_time_dict * 100} %')

    # May couse issues in multipe inheritance
    # Instance variable objects can't be add or removed dynamically
    # You can add '__dict__' or '__weakref__' as the last element in the __slots__ declaration