from collections import defaultdict, Counter

def count_fruits(fruits: list[str]) -> dict[str, int]:
    result = defaultdict(int)
    for fruit in fruits:
        result[fruit] += 1
    return result


def count_fruits2(fruits: list[str]) -> dict[str, int]:
    count = Counter(fruits)
    print(count)
    return dict(count)


def main() -> None:
    assert count_fruits(
        [
            "apple",
            "banana",
            "apple",
            "cherry",
            "banana",
            "cherry",
            "apple",
            "apple",
            "cherry",
            "banana",
            "cherry",
        ]
    ) == {"apple": 4, "banana": 3, "cherry": 4}
    assert count_fruits([]) == {}
    


if __name__ == "__main__":
    main()
