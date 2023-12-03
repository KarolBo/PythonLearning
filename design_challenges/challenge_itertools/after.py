from dataclasses import dataclass
from faker import Faker
import random
import itertools


@dataclass
class Person:
    name: str
    age: int
    city: str
    country: str


# Instantiate the Faker module
fake = Faker()

# List of possible countries
countries = [
    "UK",
    "USA",
    "Japan",
    "Australia",
    "France",
    "Germany",
    "Italy",
    "Spain",
    "Canada",
    "Mexico",
]

# Generate 1000 random Person instances
PERSON_DATA: list[Person] = [
    Person(fake.name(), random.randint(18, 70), fake.city(), random.choice(countries))
    for _ in range(1000)
]


def main() -> None:
    filtered_data: list[Person] = list(itertools.filterfalse(lambda person: person.age < 21, PERSON_DATA))
    
    filtered_data.sort(key=lambda p: p.country)

    grouped_data = itertools.groupby(filtered_data, key=lambda person: person.country)

    summary: dict[str, int] = { country: len(list(group)) for country, group in grouped_data }

    print(summary)


if __name__ == "__main__":
    main()
