"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    # list.insert() moves the element currently at index, and every element
    # after it, one position to the right before storing the new value.
    # Inserting near the beginning is O(n); inserting at the end is normally O(1)
    # amortized because few or no existing elements need to shift.
    lst.insert(index, value)


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    # This assignment treats only indexes from 0 through len(lst) - 1 as valid.
    # Checking first prevents an IndexError and avoids deleting an unintended item.
    if index < 0 or index >= len(lst):
        return None

    # pop(index) returns the removed value. Later elements shift left to fill the gap.
    return lst.pop(index)


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    # This is a linear search because values are examined sequentially from left
    # to right until a match is found or the complete list has been scanned.
    for index, current_value in enumerate(lst):
        if current_value == value:
            return index
    return -1


def run_additional_checks():
    """Use assertions to verify behavior beyond the printed starter examples."""
    values = ["B", "C"]
    insert_at(values, 0, "A")
    insert_at(values, len(values), "D")
    assert values == ["A", "B", "C", "D"]
    assert delete_at(values, 1) == "B"
    assert values == ["A", "C", "D"]
    assert delete_at(values, 50) is None
    assert search_value(values, "D") == 2
    assert search_value(values, "missing") == -1
    print("Additional insertion/deletion/search assertions: PASSED")


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS: MANUSCRIPT SECTIONS ===")
    sections = ["Opening scene", "Conflict", "Resolution"]
    print(f"Original list: {sections}")

    # Beginning insertion shifts every existing section one place to the right.
    insert_at(sections, 0, "Title page")
    print(f"After inserting at the beginning: {sections}")

    # Middle insertion shifts only the sections at and after the selected index.
    insert_at(sections, 2, "Character reveal")
    print(f"After inserting in the middle: {sections}")

    # Using len(sections) appends at the logical end without shifting existing data.
    insert_at(sections, len(sections), "Author note")
    print(f"After inserting at the end: {sections}")

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")
    removed = delete_at(sections, 0)
    print(f"Removed beginning value {removed!r}; updated list: {sections}")

    middle_index = len(sections) // 2
    removed = delete_at(sections, middle_index)
    print(f"Removed middle value {removed!r}; updated list: {sections}")

    removed = delete_at(sections, len(sections) - 1)
    print(f"Removed end value {removed!r}; updated list: {sections}")

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")
    existing_value = "Character reveal"
    existing_index = search_value(sections, existing_value)
    print(f"Found {existing_value!r} at index {existing_index}.")

    missing_value = "Epilogue"
    missing_index = search_value(sections, missing_value)
    print(f"Search for {missing_value!r} returned {missing_index} (not found).")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")
    invalid_high = delete_at(sections, 99)
    print(f"Deleting index 99 returned {invalid_high!r}; list was unchanged: {sections}")

    invalid_negative = delete_at(sections, -1)
    print(
        f"Deleting negative index -1 returned {invalid_negative!r}; "
        f"list was unchanged: {sections}"
    )

    empty_list = []
    insert_at(empty_list, 0, "First section")
    print(f"Insertion into an empty list succeeded: {empty_list}")
    removed = delete_at(empty_list, 0)
    print(f"Removed the only value {removed!r}; list is now empty: {empty_list}")
    print(f"Deletion from the empty list returned: {delete_at(empty_list, 0)!r}")

    print("\n=== ADDITIONAL AUTOMATED CHECKS ===")
    run_additional_checks()



if __name__ == "__main__":
    main()
