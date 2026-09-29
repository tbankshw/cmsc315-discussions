# Unit 7 Discussion: Sorting Algorithms

## Overview

This assignment compares Bubble Sort and Merge Sort.

## Learning Objectives

- Implement Bubble Sort
- Implement Merge Sort
- Understand divide-and-conquer
- Compare algorithm efficiency

## Requirements

1. Tested Bubble Sort and Merge Sort with two unsorted datasets.
2. Confirmed that both algorithms returned the same ascending results.
3. Demonstrated empty, already sorted, and duplicate value edge cases.
4. Analyzed the performance and tradeoffs of both algorithms.
5. Connected Merge Sort to sorting large streaming content lists.

## Implementation Summary

Bubble Sort copied the input and repeatedly compared adjacent values. It swapped values that were out of order and stopped early when a pass made no swaps. Merge Sort recursively divided a copied list into smaller halves and combined them with a stable merge operation. The program displayed the original and sorted values for two datasets and verified empty, already sorted, and duplicate value inputs.

Bubble Sort has quadratic time complexity in the average and worst cases, so its running time grows quickly with large inputs. Its early stopping behavior can be useful for small or nearly sorted lists. Merge Sort has linearithmic time complexity in every case and scales better for large collections, although it uses extra memory while merging. Merge Sort also preserves the order of equal values because the merge step selects the left value first when values are equal.

## Real World Example

A streaming platform could use Merge Sort to organize large content lists by rating or popularity. Its predictable performance makes it more suitable than Bubble Sort for millions of records. Its stable merge also keeps equally rated items in their previous order, and independent halves can be sorted across separate servers before they are merged.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

I learned how Bubble Sort and Merge Sort use different strategies to organize the same data. Bubble Sort compares neighboring values and swaps them until the list is sorted. Merge Sort divides a list into smaller parts, sorts each part, and merges the results. Implementing both algorithms helped me understand why time complexity matters as the amount of data grows.

The most challenging part was writing the merge operation because it had to track positions in two lists and include every remaining value. I handled this by testing the merge process with normal data, an empty list, an already sorted list, and duplicate values. I also compared both algorithm results to confirm they matched without changing the original input.

Bubble Sort was easier to follow and can stop early when data is already sorted, but its quadratic growth makes it inefficient for large random lists. Merge Sort required more code and extra memory, but its linearithmic performance scales much better. I would use Bubble Sort only for very small or nearly sorted data. I would use Merge Sort for large content lists where predictable speed and stable ordering are important.
