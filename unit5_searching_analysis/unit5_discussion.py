"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target, comparisons=None):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    for index, value in enumerate(lst):
        if comparisons is not None:
            comparisons[0] += 1
        if value == target:
            return index
    return -1


def binary_search(lst, target, comparisons=None):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    low = 0
    high = len(lst) - 1
    while low <= high:
        middle = (low + high) // 2
        if comparisons is not None:
            comparisons[0] += 1
        if lst[middle] == target:
            return middle
        if lst[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    return -1


def compare_searches(dataset, target):
    linear_checks = [0]
    binary_checks = [0]
    linear_index = linear_search(dataset, target, linear_checks)
    binary_index = binary_search(dataset, target, binary_checks)
    print(f"Target {target}: linear index {linear_index} in {linear_checks[0]} "
          f"checks; binary index {binary_index} in {binary_checks[0]} checks")
    assert linear_index == binary_index


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")
    manuscript_ids = [1250, 2500, 3125, 3750, 4375, 5000,
                      6250, 7500, 8750]
    print(f"Sorted manuscript IDs ({len(manuscript_ids)}): {manuscript_ids}")
    compare_searches(manuscript_ids, 8750)
    compare_searches(manuscript_ids, 4000)
    print("Both methods agree. Linear checks IDs from the start; binary "
          "checks the middle and rules out half of the sorted range.")

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")
    large_ids = list(range(100000))
    print(f"Sorted synthetic IDs: {len(large_ids):,} values (0 through 99,999)")
    compare_searches(large_ids, 99999)
    compare_searches(large_ids, 100001)
    print("Near the end or missing, linear may inspect every ID: O(n). "
          "Binary repeatedly halves the range: O(log n). "
          "These are comparison counts, not elapsed times.")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    for label, dataset, target in [
        ("empty list", [], 5),
        ("single item found", [5], 5),
        ("single item missing", [5], 8),
        ("first position", manuscript_ids, 1250),
        ("last position", manuscript_ids, 8750),
    ]:
        print(f"{label}: ", end="")
        compare_searches(dataset, target)
    print("An empty or missing result is -1; found values return their index.")

    arrival_order_ids = [8750, 1250, 5000]
    print(f"Unsorted arrival-order IDs: {arrival_order_ids}; linear search "
          f"finds 5000 at index {linear_search(arrival_order_ids, 5000)}.")
    print("Binary search is not used here because its left/right decision "
          "requires sorted data; sorting first also changes the original indexes.")


if __name__ == "__main__":
    main()
