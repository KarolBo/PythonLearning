from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import Callable


class Medium(ABC):
    @abstractmethod
    def get_heading(self):
        ...

    @abstractmethod
    def get_subheading(self):
        ...

    @abstractmethod
    def get_text(self):
        ...


ViewType = Callable[[Medium], None]

def view_list(medium: Medium) -> None:
    print(medium.get_heading())

def view_preview(medium: Medium) -> None:
    print(medium.get_heading())
    print(medium.get_subheading())

def view_full(medium: Medium) -> None:
    print(medium.get_heading())
    print(medium.get_subheading())
    print(medium.get_text())


@dataclass
class Movie(Medium):
    id: str
    title: str
    description: str
    director: str

    def get_heading(self):
        return self.title

    def get_subheading(self):
        return self.director

    def get_text(self):
        return self.description


@dataclass
class Series(Medium):
    id: str
    title: str
    summary: str
    episodes: int

    def get_heading(self):
        return self.title

    def get_subheading(self):
        return f"{self.episodes} episodes"

    def get_text(self):
        return self.summary


def main() -> None:
    media = [
        Movie(
            id="1",
            title="Spirited Away",
            description="Chihiro ...",
            director="Hayao Miyazaki",
        ),
        Series(
            id="2",
            title="Fullmetal Alchemist: Brotherhood",
            summary="Edward ...",
            episodes=64,
        ),
    ]

    for item in media:
        view_list(item)
        view_preview(item)
        view_full(item)


if __name__ == "__main__":
    main()
