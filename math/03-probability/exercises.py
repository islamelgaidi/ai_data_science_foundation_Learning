from __future__ import annotations


def bayes_theorem(probability_b_given_a: float, probability_a: float, probability_b: float) -> float:
    if probability_b == 0:
        raise ValueError("P(B) cannot be zero")
    return (probability_b_given_a * probability_a) / probability_b


def expected_value(values: list[float], probabilities: list[float]) -> float:
    if len(values) != len(probabilities):
        raise ValueError("Values and probabilities must have the same length")
    return sum(value * probability for value, probability in zip(values, probabilities))


def run_examples() -> None:
    values = [0, 1]
    probabilities = [0.7, 0.3]
    print("Expected value:", expected_value(values, probabilities))
    print("Bayes theorem example:", bayes_theorem(0.9, 0.01, 0.05))


if __name__ == "__main__":
    run_examples()