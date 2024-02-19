

class Vehicle:
    def __init__(self, name: str) -> None:
        self.name = name
        print(f'Creating a Vehicle: {name}')

    def go(self):
        print('Somehow moving...')
        assert not hasattr(super(), 'go')


class Car(Vehicle):
    def __init__(self, n_wheels: int,  **kwargs) -> None:
        super().__init__(**kwargs)
        self.wheels = n_wheels
        print(f'Creating a Car: {self.name}')

    def go(self):
        print('Riding...')
        super().go()


class Boat(Vehicle):
    def __init__(self, n_props, **kwargs) -> None:
        super().__init__(**kwargs)
        self.propellers = n_props
        print(f'Creating a Boat: {self.name}')

    def go(self):
        print('Swimming...')
        super().go()


class Amfibii(Car, Boat):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        print(f'Creating an Amfibii: {self.name}')

    def go(self):
        print('Riding or swimming...')
        super().go()


my_vehicle = Amfibii(name='Mazda', n_wheels=4, n_props=2)
my_vehicle.go()