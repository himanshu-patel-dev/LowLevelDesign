## Problem Statement
We have to do low level design for a Cache system (In Memory Database). Cache that we will design will have to support following operations:

- `put`: Put a value against a key in the cache. Create the entry if not present else update.
- `get`: Search for given key and returns it's value if present else return None.
- `delete`: Remove a key if present.
- `keys`: Get all the keys in database.
- `search`: Search and return the key which have given value else return nothing.

Should be extensible for changes and follow SOLID desgin principles.
