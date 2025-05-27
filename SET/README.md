# add()

* Adds an element to the set.

**Syntax:**

* set.add(element)

**Parameters:**

* element - The element to be added to the set

**Return Value:**

* None (modifies the set in place)

**Notes:**

* If the element already exists in the set, the set remains unchanged

* The element must be hashable (immutable types like strings, numbers, tuples)

# clear()

* Removes all elements from the set.

**Syntax:**

* set.clear()

**Parameters:**
* None

**Return Value:**
* None (modifies the set in place)

# copy()
* Returns a shallow copy of the set.

**Syntax:**

* new_set = set.copy()

**Parameters:**
* None

**Return Value:**
* A new set containing the same elements

# difference()
* Returns a new set containing elements that are in the first set but not in the others.

**Syntax:**
* result_set = set.difference(*others)

**Parameters:**

* others - One or more sets or iterables to compare against

**Return Value:**
* A new set with the difference

**Alias:**
* Can also be written using the - operator: a - b - c

# difference_update()
* Updates the set by removing elements found in others.

**Syntax:**

* set.difference_update(*others)

**Parameters:**

* others - One or more sets or iterables

**Return Value:**
* None (modifies the set in place)

**Alias:**
* Can also be written using -= operator: a -= b

# discard
Removes an element from the set if it is present.

**Syntax:**

* set.discard(element)
**Parameters:**

* element - The element to remove

**Return Value:**
* None

**Notes:**

* Does not raise an error if the element is not found

* Similar to remove() but doesn't raise KeyError for missing elements

# intersection()
Returns a new set with elements common to all sets.

**Syntax:**

* result_set = set.intersection(*others)
**Parameters:**

* others - One or more sets or iterables

**Return Value:**
* A new set with common elements

**Alias:**
Can also be written using & operator: a & b

# intersection_update()
Updates the set with the intersection of itself and others.

**Syntax:**

* set.intersection_update(*others)
**Parameters:**

* others - One or more sets or iterables

**Return Value:**
* None (modifies the set in place)

**Alias:**
Can also be written using &= operator: a &= b

# isdisjoint()
Returns True if the set has no elements in common with other.

**Syntax:**

* set.isdisjoint(other)
**Parameters:**

* other - Another set or iterable

**Return Value:**
* Boolean (True if no common elements)

# issubset()
Returns True if all elements of the set are in other.

**Syntax:**

* set.issubset(other)
**Parameters:**

* other - Another set or iterable

**Return Value:**
* Boolean

**Alias:**
* Can also be written using <= operator: a <= b

# issuperset()
Returns True if all elements of other are in the set.

**Syntax:**

* set.issuperset(other)
**Parameters:**

* other - Another set or iterable

**Return Value:**
* Boolean

**Alias:**
* Can also be written using >= operator: a >= b

# pop()
Removes and returns an arbitrary element from the set.

**Syntax:**

* element = set.pop()
**Parameters:**
* None

**Return Value:**
* The removed element

# remove()
Removes an element from the set. Raises KeyError if not found.

**Syntax:**

* set.remove(element)
**Parameters:**

* element - The element to remove

**Return Value:**
* None

**Notes:**

* Raises KeyError if element is not found

* Use discard() if you don't want an error for missing elements

# symmetric_difference
Returns a new set with elements in either set but not both.

**Syntax:**

* result_set = set.symmetric_difference(other)
**Parameters:**

* other - Another set or iterable

**Return Value:**
* A new set with symmetric difference

**Alias:**
* Can also be written using ^ operator: a ^ b

# symmetric_difference_update()
Updates the set with elements in either set but not both.

**Syntax:**

* set.symmetric_difference_update(other)
**Parameters:**

* other - Another set or iterable

**Return Value:**
* None (modifies the set in place)

**Alias:**
* Can also be written using ^= operator: a ^= b

# union()
Returns a new set containing all distinct elements from all sets.

**Syntax:**

* result_set = set.union(*others)
**Parameters:**

* others - One or more sets or iterables

**Return Value:**
* A new set with all distinct elements

**Alias:**
* Can also be written using | operator: a | b

# update
The update() method in Python is an essential tool when working with sets. This method allows the merging of two or more sets, integrating all unique elements from each set involved into a single set without duplication. The update() method in Python adds elements from a set or any iterable (like lists, tuples, or other sets) to the set on which update() is called. This method modifies the set in place, meaning it doesn't create a new set but changes the original one.

**update() Parameter**
* The update() method can take any number of arguments.
**update() Return Value**
* The update() method doesn't return any value.
**update() Syntax**
* A.update(B)