# Unit 2 Discussion: Stacks and Queues

## Overview

This project implemented a list-backed stack and a `deque`-backed queue. The demonstrations modeled editorial revision history with LIFO behavior and editorial request intake with FIFO behavior.

## Implementation Documentation

### Stack

The `Stack` class stored values in a private-style Python list named `_items`. `push()` appended a value to the end, and `pop()` removed the value from that same end, producing last-in, first-out behavior. `peek()` returned the newest value without removing it, `is_empty()` reported whether the list contained data, and the student-created `size()` extension returned the number of stored values.

List `append()` and end-position `pop()` were used because both normally run in amortized O(1) time. A stack containing `n` values used O(n) memory.

### Queue

The `Queue` class stored values in `collections.deque`. `enqueue()` appended a value at the back, while `dequeue()` used `popleft()` to remove the oldest value from the front, producing first-in, first-out behavior. `front()`, `is_empty()`, and the student-created `size()` method provided non-destructive inspection.

A deque was selected instead of removing index zero from a list. Both `append()` and `popleft()` run in O(1) time, while a list's front removal would require shifting the remaining values. A queue containing `n` values used O(n) memory.

## Demonstrations and Edge Cases

The stack demo pushed four publishing revisions and removed them newest-first. The queue demo enqueued four editorial requests and processed them oldest-first. Both demos tested an empty removal, an empty inspection, and a one-item structure that became empty after removal. Invalid empty operations raised descriptive `IndexError` exceptions and were caught so the program explained each problem without crashing.

The `run_additional_checks()` function used assertions to verify `peek()`, `front()`, `size()`, `pop()`, and `dequeue()` behavior beyond the printed examples.

## Real-World Application

A publishing application could use a stack to undo recent manuscript revisions because the newest change must be reversed first. It could use a queue for editorial requests because the request that arrived first should normally be processed first. The same structures could support browser history, customer-service tickets, print jobs, or task scheduling.

## Discussion Board Reflection

Completing this assignment taught me how implementation choices create the different behaviors of stacks and queues. I used a Python list for the stack because appending and removing from the end naturally produced last-in, first-out behavior. I used `deque` for the queue because `append()` and `popleft()` efficiently produced first-in, first-out behavior without shifting every remaining item. My main challenge was deciding how empty operations should behave. I handled them with descriptive `IndexError` exceptions and caught those exceptions in the demonstrations, so invalid operations were visible without terminating the program. The publishing scenario made the distinction practical. A revision history works as a stack because the newest manuscript change should be the first one undone. Editorial requests work as a queue because the oldest request should normally be processed first. Both structures grow linearly with the number of stored items, but their removal order serves different needs. In future applications, I could reuse a stack for browser navigation or undo tools and a queue for support tickets, print jobs, or scheduled work.
