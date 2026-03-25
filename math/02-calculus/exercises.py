from __future__ import annotations


def numerical_derivative(function, x: float, step: float = 1e-5) -> float:
    return (function(x + step) - function(x - step)) / (2 * step)


def square(x: float) -> float:
    return x * x


def cubic(x: float) -> float:
    return x * x * x


def run_examples() -> None:
    x_value = 3.0
    print("Derivative of x^2 at x=3:", numerical_derivative(square, x_value))
    print("Derivative of x^3 at x=3:", numerical_derivative(cubic, x_value))


if __name__ == "__main__":
    run_examples()