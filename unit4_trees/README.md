# Unit 4 Discussion: Binary Search Trees

## Overview

This activity implemented a recursive Binary Search Tree (BST) as a catalog of
unique manuscript IDs. The program inserted 11 IDs, searched for present and
missing IDs, and displayed the IDs in sorted order.

## Implementation

- The `Node` class stored a value and references to its left and right children.
- Recursive insertion placed smaller IDs in the left subtree and larger IDs in
  the right subtree. Duplicate IDs were ignored.
- Recursive search followed only the subtree that could contain the requested ID.
- In-order traversal visited the left subtree, node, and right subtree, which
  produced ascending output because of the BST ordering rule.

## Demonstration and Edge Cases

The program inserted IDs on both sides of the root and tested two successful and
two unsuccessful searches. It also demonstrated an empty traversal, a search of
an empty tree, duplicate insertion, and a single-node tree. The output explained
the result of each operation.

## Discussion Board Reflection

Completing this activity helped me understand how a Binary Search Tree used its
ordering rule during insertion, searching, and traversal. I modeled a manuscript
catalog in which every manuscript had a unique numerical ID. Recursive insertion
placed smaller IDs in the left subtree and larger IDs in the right subtree. The
most challenging part was understanding why each recursive insertion had to
return the current node. Tracing a few insertions by hand showed me that the
returned reference reconnected each child to its parent as the calls completed.

The in-order traversal demonstrated the structure clearly because visiting the
left subtree, current node, and right subtree returned every ID in ascending
order. I also tested empty-tree operations, a duplicate ID, and a single-node
tree. The empty tree safely returned an empty list or `False`, while the duplicate
was ignored so IDs remained unique. Compared with a linear list, a reasonably
balanced BST can reduce the remaining search space after each comparison and
provide average O(log n) search performance. However, sequential insertions can
produce a one-sided tree that behaves like a linked list, causing search time to
degrade to O(n).
