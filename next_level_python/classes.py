from dataclasses import dataclass, field


# frozen=True
@dataclass(kw_only=True)
class Person:
    name: str
    address: str
    id: str = field(init=False, repr=False) # id is not a constructor parameter, not printed
    email_addresses: list[str] = field(default_factory=list)

    def __post_init__(self):
        self.id = self._generate_id()

    # def __init__(self, name: str, address: str):
    #     self.id = self._generate_id()
    #     self.name = name
    #     self.address = address
    #     self.email_addresses = []

    @property
    def search_string(self):
        return f'{self.name} {self.address}'
    
    @search_string.setter
    def search_string(self, new_value: str) -> None:
        tokens = new_value.split(' ')
        m = len(tokens) // 2
        self.name, self.address = ' '.join(tokens[:m]), ' '.join(tokens[m:])

    @staticmethod
    def _generate_id():
        return '123456789'
    
    def __str__(self):
        return self.name
    
    
person = Person(name='Karol', address='Adliswil')
print(person)
print(person.search_string)
person.search_string = "Agnieszka Borkowska 8134 Adliswil"
print(person.search_string)

print(person) 
print(repr(person))
print(f'{person!r}')