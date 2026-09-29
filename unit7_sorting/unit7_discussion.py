"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================

STUDENT INSTRUCTIONS:

This project explores two fundamental sorting algorithms:
- Bubble Sort (iterative, comparison-based)
- Merge Sort (recursive, divide-and-conquer)

Your goal is to demonstrate both your coding ability and your
understanding of algorithm efficiency and behavior.
"""


def bubble_sort(lst):
    """
    TODO (Student):
    Implement Bubble Sort.

    Requirements:
    - Create a copy of the original list.
    - Compare adjacent elements.
    - Swap elements when they are out of order.
    - Continue until the list is sorted.
    - Return the sorted list.
    - Add meaningful comments.

    """
    sorted_list = lst.copy()
    for end in range(len(sorted_list) - 1, 0, -1):
        swapped = False
        for index in range(end):
            if sorted_list[index] > sorted_list[index + 1]:
                sorted_list[index], sorted_list[index + 1] = (
                    sorted_list[index + 1],
                    sorted_list[index],
                )
                swapped = True
        if not swapped:
            break
    return sorted_list


def merge_sort(lst):
    """
    TODO (Student):
    Implement Merge Sort.

    Requirements:
    - Use recursion.
    - Divide the list into smaller halves.
    - Sort each half recursively.
    - Merge the sorted halves together.
    - Return the sorted list.
    - Add meaningful comments.

    """
    if len(lst) <= 1:
        return lst.copy()

    midpoint = len(lst) // 2
    left = merge_sort(lst[:midpoint])
    right = merge_sort(lst[midpoint:])
    return merge(left, right)


def merge(left, right):
    """
    TODO (Student):
    Implement the merge step used by Merge Sort.

    Requirements:
    - Compare values from the left and right lists.
    - Build a new sorted result list.
    - Append any remaining values.
    - Return the merged sorted list.
    - Add meaningful comments.
    """
    result = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result


def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    # ===============================
    # TODO (Student): DATASET #1
    # ===============================
    #
    # Requirements:
    # 1. Create an unsorted list containing at least 7 values.
    # 2. Display the original list.
    # 3. Sort the list using Bubble Sort.
    # 4. Sort the same list using Merge Sort.
    # 5. Clearly label and display all results.

    print("\n=== DATASET #1 ===")
    dataset_one = [42, 17, 8, 99, 23, 4, 61]
    print(f"Original: {dataset_one}")
    print(f"Bubble Sort: {bubble_sort(dataset_one)}")
    print(f"Merge Sort: {merge_sort(dataset_one)}")

    # ===============================
    # TODO (Student): DATASET #2
    # ===============================
    #
    # Requirements:
    # 1. Create a second dataset.
    # 2. Use different values than Dataset #1.
    # 3. Sort using both algorithms.
    # 4. Compare the results.

    print("\n=== DATASET #2 ===")
    dataset_two = [58, 12, 73, 31, 6, 44, 19, 85]
    bubble_result = bubble_sort(dataset_two)
    merge_result = merge_sort(dataset_two)
    print(f"Original: {dataset_two}")
    print(f"Bubble Sort: {bubble_result}")
    print(f"Merge Sort: {merge_result}")
    print(f"Results match: {bubble_result == merge_result}")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Already sorted list
    # - Reverse-sorted list
    # - List with duplicate values
    # - Single-element list
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    edge_cases = {
        "Empty list": [],
        "Already sorted list": [2, 4, 6, 8],
        "Duplicate values": [5, 2, 5, 1, 2],
    }
    for label, values in edge_cases.items():
        print(f"{label}: {values}")
        print(f"Bubble Sort: {bubble_sort(values)}")
        print(f"Merge Sort: {merge_sort(values)}")




if __name__ == "__main__":
    main()
