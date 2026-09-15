# Unit 5 Discussion: Search Algorithms

## Overview

I implemented and compared linear and binary search using a manuscript-ID lookup.
Both functions returned the target's index or `-1` when it was missing.

## How It Worked

Linear search checked IDs from the start until it found a match or reached the
end. Its worst case grew with the list size, O(n). Binary search required sorted
IDs and checked the midpoint of the remaining index range. It moved the low or
high boundary past that midpoint, discarding half the range each time, so its
worst case grew as O(log n). Comparison counters made the difference visible
without relying on noisy elapsed-time measurements.

## Tests and Results

I tested a small sorted catalog of nine manuscript IDs and a large sorted list
of 100,000 synthetic IDs. Both algorithms returned the same indexes for found
and missing targets. For the last ID in the large list, linear search made
100,000 checks while binary search made 17. A missing ID above the list's
maximum required 100,000 linear checks but also only 17 binary checks. I also
tested an empty list, found and missing single-item lists, and first and last
positions. An unsorted arrival-order list showed that linear search could work
without preparation; I did not run binary search on that list because its
half-elimination rule would not be valid.


## Discussion Board Reflection

This activity taught me that search speed depended on how data was organized.
For manuscript IDs, linear search walked through a list in arrival order, while
binary search narrowed a sorted list. The trickiest part was updating the low
and high indexes without rechecking the midpoint. Testing first and last
positions, empty lists, and missing values helped me check those boundaries.

On a small list, linear search was easy to use and could find an early value
immediately. It also made sense for a short, unsorted list of new manuscript
submissions that I needed to check only once. Sorting first would cost time and
change its arrival-order indexes. For a large catalog already sorted by ID and
searched repeatedly, binary search was better: every comparison removed about
half the possible positions. The 100,000-ID test made that difference concrete.
Binary search could not reliably use an unsorted list, or one sorted by title
instead of ID, because the midpoint would not identify the correct half. I
would choose based on list size, ordering, and how often I needed to search.
