import pytest

from solutions.problem6 import find_max


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, 4, 5], 5),
        ([-1, -5, -2], -1),
        ([0], 0),
    ],
)
def test_find_max(nums: list[int], expected: int) -> None:
    assert find_max(nums) == expected


def test_find_max_raises_for_empty_list() -> None:
    with pytest.raises(ValueError):
        find_max([])


def test_find_max_all_negative_strictly_decreasing() -> None:
    assert find_max([-10, -30, -20, -50]) == -10


def test_find_max_large_magnitude_mix() -> None:
    assert find_max([10**6, -10**12, 10**3, 999_999]) == 10**6


def test_find_max_duplicate_max_values() -> None:
    assert find_max([42, 17, 42, 3]) == 42


def test_find_max_negative_and_positive_mix() -> None:
    assert find_max([-100, 0, -50, 75, 10]) == 75


# ============================================================================
# SPEC-GUIDED TESTS (Generated from formal specifications in EX3)
# ============================================================================


def test_spec_guided_result_in_list() -> None:
    """Spec 1 & 4: Verify result is an element of the input list."""
    nums = [5, 2, 8, 1, 9]
    res = find_max(nums)
    assert res in nums


def test_spec_guided_result_greater_equal_all() -> None:
    """Spec 2 & 4: Verify result is >= all elements."""
    nums = [3, 7, 2, 9, 4]
    res = find_max(nums)
    assert all(res >= x for x in nums)


@pytest.mark.parametrize("nums", [[42], [0], [-5], [100]])
def test_spec_guided_single_element_list(nums: list[int]) -> None:
    """Spec 3: For single-element lists, result equals that element."""
    res = find_max(nums)
    assert res == nums[0]


@pytest.mark.parametrize("nums", [
    [1, 2, 3],
    [-10, -5, -1],
    [0, 0, 0],
    [100, 50, 75, 25],
])
def test_spec_guided_combined_property(nums: list[int]) -> None:
    """Spec 4: Combined property - res in nums and res >= all elements."""
    res = find_max(nums)
    assert res in nums
    assert all(res >= x for x in nums)


def test_spec_guided_all_elements_equal() -> None:
    """Verify spec holds when all elements are equal."""
    nums = [7, 7, 7, 7]
    res = find_max(nums)
    assert res in nums
    assert all(res >= x for x in nums)
    assert res == 7


def test_spec_guided_negative_numbers() -> None:
    """Verify spec holds for negative numbers."""
    nums = [-1, -5, -3, -2]
    res = find_max(nums)
    assert res in nums
    assert all(res >= x for x in nums)


def test_spec_guided_mixed_signs() -> None:
    """Verify spec holds for mixed positive and negative numbers."""
    nums = [-10, 5, -3, 8, -1]
    res = find_max(nums)
    assert res in nums
    assert all(res >= x for x in nums)

