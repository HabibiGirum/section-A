# clear()

Removes all key-value pairs from the dictionary, leaving it empty.

**Arguments**

* None.

**Return Value**

* None (modifies the original dictionary in place).

**Syntax**

* dict.clear()

# fromkeys()

* Creates a new dictionary with keys from an iterable (like a list or tuple) and sets all values to a specified default.

**Arguments**

* keys (iterable): Keys to initialize.

* value (optional): Default value for all keys (defaults to None).

**Return Value**

* A new dictionary with the provided keys and the same default value.

**Syntax**

* dict.fromkeys(keys[, value])

# get()

* Safely retrieves the value associated with a key. If the key doesn’t exist, it returns a default value instead of raising a KeyError.

**Arguments**

* key: The key to search for.

* default (optional): Value to return if the key is missing (defaults to None).

**Return Value**

* The value for the key if found; otherwise, the default value.

**Syntax**

* dict.get(key[, default])

# items()

* Returns a dynamic view object of the dictionary’s (key, value) pairs as tuples. This view reflects any changes made to the dictionary and is useful for iterations or membership checks.

**Arguments**

* None.

**Return Value**

* A view object that displays (key, value) pairs in the dictionary.

**Syntax**

* dict.items()

# keys()

* Returns a dynamic view object of all keys in the dictionary. The view updates automatically if the dictionary changes, making it efficient for iterations or checking key existence.

**Arguments**

* None.

**Return Value**

* A view object that displays all keys in the dictionary.

**Syntax**

* dict.keys()

# pop()

* Removes a specified key from the dictionary and returns its value. If the key doesn’t exist, it raises a KeyError unless a default value is provided.

**Arguments**

* key: The key to remove.

* default (optional): Value to return if the key is missing (avoids KeyError).

**Return Value**

* The value of the removed key, or default if provided (else raises KeyError).

**Syntax**

* dict.pop(key[, default])

# popitem()

Removes and returns the last inserted (key, value) pair as a tuple (LIFO order in Python 3.7+). Useful for destructively iterating over a dictionary.

**Arguments**

* None.

**Return Value**

* A tuple (key, value) of the last inserted item. Raises KeyError if the dictionary is empty.

**Syntax**

* dict.popitem()

# setdefault()

* Returns the value of a key if it exists. If not, it inserts the key with a specified default value (similar to get(), but modifies the dictionary).

**Arguments**

* key: The key to check/insert.

* default (optional): Value to set if the key is missing (defaults to None).

**Return Value**

* The existing value if the key is found; otherwise, the newly set default value.

**Syntax**

* dict.setdefault(key[, default])

# update()

* Merges a dictionary or an iterable of key-value pairs into the current dictionary. Overwrites existing keys with new values.

**Arguments**

* iterable: Another dictionary or iterable of (key, value) pairs.

**Return Value**
* None (modifies the original dictionary in place).

**Syntax**

* dict.update([iterable])

# values()

* Returns a dynamic view object of all values in the dictionary. The view updates in real-time as the dictionary changes, making it memory-efficient for iterations.

**Arguments**

* None.

**Return Value**

* A view object that displays all values in the dictionary.

**Syntax**

* dict.values()