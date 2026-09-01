"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self._items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        # Appending makes this value the last item in and the first available out.
        self._items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack.")
        return self._items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        if self.is_empty():
            raise IndexError("Cannot peek at an empty stack.")
        # Index -1 reads the newest item without changing the stack.
        return self._items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self._items) == 0

    def size(self):
        """Student-created extension that reports the current number of items."""
        return len(self._items)


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self._items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        # New values wait at the back while the oldest value stays at the front.
        self._items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue.")
        return self._items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        if self.is_empty():
            raise IndexError("Cannot view the front of an empty queue.")
        # Index 0 reads the oldest value without removing it.
        return self._items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self._items) == 0

    def size(self):
        """Student-created extension that reports the current number of items."""
        return len(self._items)


def run_additional_checks():
    """Run assertions beyond the printed starter demonstrations."""
    test_stack = Stack()
    test_stack.push("first revision")
    test_stack.push("second revision")
    assert test_stack.peek() == "second revision"
    assert test_stack.size() == 2
    assert test_stack.pop() == "second revision"
    assert test_stack.peek() == "first revision"

    test_queue = Queue()
    test_queue.enqueue("first request")
    test_queue.enqueue("second request")
    assert test_queue.front() == "first request"
    assert test_queue.size() == 2
    assert test_queue.dequeue() == "first request"
    assert test_queue.front() == "second request"

    print("Additional LIFO/FIFO assertion checks: PASSED")


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.
    print("\n=== STACK DEMO: EDITORIAL REVISION HISTORY ===")
    revision_stack = Stack()
    revisions = ["Draft 1", "Draft 2", "Copyedit", "Author approval"]
    for revision in revisions:
        revision_stack.push(revision)
        print(f"Pushed {revision!r}; current top is {revision_stack.peek()!r}.")

    print(f"Stack size after four pushes: {revision_stack.size()}")
    removal_order = []
    while not revision_stack.is_empty():
        removal_order.append(revision_stack.pop())
    print(f"LIFO removal order (newest revision first): {removal_order}")

    try:
        revision_stack.pop()
    except IndexError as error:
        print(f"Empty-stack pop handled safely: {error}")

    try:
        revision_stack.peek()
    except IndexError as error:
        print(f"Empty-stack peek handled safely: {error}")

    single_revision = Stack()
    single_revision.push("Only draft")
    print(f"Single-item stack removed: {single_revision.pop()!r}")
    print(f"Single-item stack is now empty: {single_revision.is_empty()}")

    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.
    print("\n=== QUEUE DEMO: EDITORIAL REQUEST INTAKE ===")
    request_queue = Queue()
    requests = [
        "Review chapter outline",
        "Check source citation",
        "Approve cover copy",
        "Schedule publication",
    ]
    for request in requests:
        request_queue.enqueue(request)
        print(f"Enqueued {request!r}; front remains {request_queue.front()!r}.")

    print(f"Queue size after four enqueues: {request_queue.size()}")
    processing_order = []
    while not request_queue.is_empty():
        processing_order.append(request_queue.dequeue())
    print(f"FIFO processing order (oldest request first): {processing_order}")

    try:
        request_queue.dequeue()
    except IndexError as error:
        print(f"Empty-queue dequeue handled safely: {error}")

    try:
        request_queue.front()
    except IndexError as error:
        print(f"Empty-queue front handled safely: {error}")

    single_request = Queue()
    single_request.enqueue("Only request")
    print(f"Single-item queue removed: {single_request.dequeue()!r}")
    print(f"Single-item queue is now empty: {single_request.is_empty()}")

    print("\n=== ADDITIONAL AUTOMATED CHECKS ===")
    run_additional_checks()

if __name__ == "__main__":
    main()
