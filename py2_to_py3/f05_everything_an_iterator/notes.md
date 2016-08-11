Everything is an Iterator

- Functions that returned lists will now return iterators
- This cuts down on the time/memory needed to process the values
- If you need a list from the function, just call `list()` on the returned value
- methods that no longer return lists: zip, map, filter, dict: keys, values, items