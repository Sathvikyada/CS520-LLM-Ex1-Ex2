import pytest

from solutions.problem8 import is_prime


@pytest.mark.parametrize(
    "n, expected",
    [
        (2, True),
        (9, False),
        (13, True),
        (1, False),
        (0, False),
    ],
)
def test_is_prime(n: int, expected: bool) -> None:
    assert is_prime(n) is expected


def test_is_prime_even_composite() -> None:
    assert is_prime(4) is False


def test_is_prime_negative_number() -> None:
    assert is_prime(-7) is False


def test_is_prime_large_prime() -> None:
    assert is_prime(97) is True


def test_is_prime_square_of_prime() -> None:
    assert is_prime(121) is False


def test_is_prime_carmichael_number() -> None:
    assert is_prime(561) is False


# ============================================================================
# SPEC-GUIDED TESTS (Generated from formal specifications in EX3)
# ============================================================================


@pytest.mark.parametrize("n", [0, 1, -1, -5])
def test_spec_guided_non_prime_less_equal_one(n: int) -> None:
    """Spec 1: Numbers <= 1 are not prime."""
    res = is_prime(n)
    assert (n <= 1) == (not res)


def test_spec_guided_two_is_prime() -> None:
    """Spec 2: 2 is the only even prime number."""
    n = 2
    res = is_prime(n)
    assert (n == 2) == res


@pytest.mark.parametrize("n", [4, 6, 8, 10, 12, 14, 16, 18, 20])
def test_spec_guided_even_greater_than_two_not_prime(n: int) -> None:
    """Spec 3: Even numbers > 2 are not prime."""
    res = is_prime(n)
    assert (n % 2 == 0 and n > 2) == (not res)


@pytest.mark.parametrize("n", [3, 5, 7, 11, 13, 17, 19, 23, 29, 31])
def test_spec_guided_prime_no_divisors(n: int) -> None:
    """Spec 4: Prime if no divisors in range [2, sqrt(n)]."""
    res = is_prime(n)
    expected = (n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1)))
    assert expected == res


@pytest.mark.parametrize("n, expected", [(3, True), (5, True), (7, True)])
def test_spec_guided_small_known_primes(n: int, expected: bool) -> None:
    """Spec 5: Small known primes return True."""
    res = is_prime(n)
    assert (n == 3 or n == 5 or n == 7) == res


@pytest.mark.parametrize("n", [9, 15, 21, 25, 27, 33, 35, 49])
def test_spec_guided_composite_has_divisors(n: int) -> None:
    """Verify composite numbers have divisors in range [2, sqrt(n)]."""
    res = is_prime(n)
    has_divisor = any(n % i == 0 for i in range(2, int(n**0.5) + 1))
    if has_divisor and n > 1:
        assert res is False


def test_spec_guided_boundary_zero_one() -> None:
    """Test boundary cases for spec 1."""
    assert is_prime(0) is False
    assert is_prime(1) is False

