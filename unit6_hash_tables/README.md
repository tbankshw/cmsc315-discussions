# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This activity used a Python dictionary to model a restaurant reservation system. Each confirmation number served as a unique key, and each guest record served as its value. The program inserted six reservations, retrieved two existing reservations, updated a party size, deleted a canceled reservation, and displayed the table after each change.

## Operations Demonstrated

- Inserted key-value pairs for reservation confirmation numbers and guest details
- Retrieved reservations using their confirmation numbers
- Updated an existing reservation without creating a duplicate key
- Deleted an existing reservation with `pop()`
- Safely handled a missing lookup and a missing deletion
- Tested an empty dictionary
- Reassigned a repeated key to show that one key keeps one current value

## Real-World Scenario

A restaurant host can use this structure to find a reservation quickly by confirmation number during a busy dinner period. The confirmation number gives the system a direct identifier instead of requiring the host to scan every reservation. Updates can change a party size, and deletions can remove canceled reservations while the other records remain available.

## Reflection

I learned how Python dictionaries provide the main operations of a hash table through key-value storage. The reservation confirmation number acts as the key, and Python applies a hash function to help locate the related guest record. This usually makes insertion, lookup, update, and deletion average O(1) operations. My main challenge was handling missing keys without stopping the program. I solved this by using `get()` with a default message for lookups and `pop()` with a default value for deletions. I also tested an empty dictionary and a repeated key. Assigning the repeated key did not create a second reservation; it replaced the earlier value. A collision occurs when different keys map to the same internal location. Python resolves collisions internally, but many collisions can require extra comparisons and reduce performance toward O(n) in poor cases. Keeping keys stable and allowing the dictionary to resize helps preserve efficient access. This activity showed why hash tables work well for reservations, inventories, user profiles, and other systems that retrieve records by unique identifiers.

## Run

```bash
python3 unit6_discussion.py
```

The output labels every operation and shows how the reservation table changes.
