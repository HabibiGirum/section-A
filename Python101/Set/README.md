# Sets 
Sets are python data type used to store unique, unordered collections of data. They are similar to mathematical sets and support operations like union, intersection, and difference.

# Set Methods
# set.add()
This set method is used to add a single item or an element (that is placed in the parenthesis) in to the set. It will modify the set with the added item.

# set.difference()
This method creates a new set then returns the new set containing elements in the original set but not in the others. Keep in mind that this method accepts multiple sets as arguments and  the original sets remain unchanged.

# set.difference_update()
Unlike the difference() method this method doesn't make a new set, rather it will modify the original set by removing the items that are presented in the other set. 

# set.dicard()
This set method is used to modify the given set by removing a specified element from the set if it exists.

# set.intersect()
Going back to our elementery school knowledge this method is as function we used in sets to find elements that are similar in different given sets. This method is used to return a new set with elements common to all sets. It doesn't modify the sets.

# set.intersect_update()
Opposite to the above defined method this one Modifies the set by keeping only elements common to all specified sets.

# set.union()
This is another topic that we learned in elementary. We use this method to create a new set with combination of elements from multiple sets. When doing that it excludes duplicates.

# set.symmetric_difference()
This method is used to compare between two sets by returning elements that are in either set, but not both. It is done by making a new set so the original sets will not be modified.

# set.symmetric_difference_update()
This one is similar with the above one except this one updates the original set to keep only elements in either set, but not both. Meaning this method will modify the original set.

# set.update()
This method is used to update the set by adding new elements from the iterables (i.e.list, tuple, set, etc that are put in the parenthesis) to the set. 
As the name impliy the method will update or modify the original set.

# set.pop()
This method is used to remove and return an arbitrary element (i.e. unpredictable) from the set. It will modify the original set are we can call it to return us the removed elements. 

# set.remove()
Unlike the pop() method this one removes a specified element from the set. It will modify the original set but can't call for it (if we do we will get "None").

# isdisjoint()
This method checks if two sets have no common elements. It returns "True" if the sets share no elements or "False" if at least one common element exists.

# issubset()
This on checks if all elements of the set are present in other. Returns "True" if the current set is a subset of other or "False" if at least one element is missing in other.	

# issuperset()
This checks if the set contains all elements of other. It returns "True" if the current set is a superset of other or "False" if at least one element of other is missing.

->The methods that are described below are useful but  less common or you might say they are not the core methods used on sets. The core methods are already coverd. 

# set.copy()
This make a new set that returns a shallow copy of the original set.

# set.clear()
This method is used to modify the set by clearing or removing  all elements from the set.

# set.len()
Used to determine the number of elements in the set.