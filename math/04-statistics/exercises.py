from __future__ import annotations


def mean(values: list[float]) -> float:
    if not values:
        raise ValueError("Values cannot be empty")
    return sum(values) / len(values)


def variance(values: list[float]) -> float:
    average = mean(values)
    return sum((value - average) ** 2 for value in values) / len(values)


def run_examples() -> None:
    sample = [2, 4, 4, 4, 5, 5, 7, 9]
    print("Mean:", mean(sample))
    print("Variance:", variance(sample))


if __name__ == "__main__":
    run_examples()