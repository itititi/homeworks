import pytest


def sum_of_digits(number):
    return sum([int(digit) for digit in str(number)])


@pytest.mark.parametrize("number, expected_sum", [
    (12345, 15),
    (101010, 3),
    (9876543210, 45),
])
def test_sum_of_digits(number, expected_sum):
    assert sum_of_digits(number) == expected_sum
