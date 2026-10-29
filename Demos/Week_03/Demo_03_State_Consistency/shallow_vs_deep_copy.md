# Shallow Copy vs. Deep Copy

A beginner's guide to copying data in Python. Companion to
[State Consistency](README.md).

## The Big Idea

In Python, a variable is a **name tag** attached to an object, not a box that
holds the object. When you "copy" something, you need to ask:

> Did I get a **new object**, or just **another name tag** on the same object?

For simple, flat data, the answer rarely matters. For **nested** data, like a
list of lists or a dictionary of dictionaries, the answer matters a lot.

## Three Ways to "Copy"

| Approach | Code | New outer container? | New inner objects? |
| --- | --- | --- | --- |
| Assignment (alias) | `b = a` | No | No |
| Shallow copy | `b = a.copy()` or `copy.copy(a)` | **Yes** | No (shared) |
| Deep copy | `b = copy.deepcopy(a)` | **Yes** | **Yes** |

- **Assignment** makes a second name for the *same* object.
- A **shallow copy** makes a new outer container, but its items still refer to
  the *same* inner objects as the original.
- A **deep copy** makes a new outer container *and* new copies of everything
  inside it, all the way down.

Here is how the memory looks for a list of two equipment records:

```text
Assignment:   original ──┐
                         ├──► [ outer list ] ──► E01 record, E02 record
              alias ─────┘

Shallow:      original ──► [ outer list A ] ──┐
                                              ├──► E01 record, E02 record  (shared!)
              shallow ───► [ outer list B ] ──┘

Deep:         original ──► [ outer list A ] ──► E01 record,  E02 record
              deep ──────► [ outer list B ] ──► E01 copy,    E02 copy     (independent)
```

## Example 1: Comparing All Three

```python
import copy

original = [["E01", "Ready"], ["E02", "Ready"]]

alias = original                 # same list
shallow = copy.copy(original)    # new outer list, same inner lists
deep = copy.deepcopy(original)   # new outer list, new inner lists

# Change something INSIDE an inner list.
original[0][1] = "On loan"

print("original:", original)
print("alias:   ", alias)
print("shallow: ", shallow)
print("deep:    ", deep)
```

Output:

```text
original: [['E01', 'On loan'], ['E02', 'Ready']]
alias:    [['E01', 'On loan'], ['E02', 'Ready']]
shallow:  [['E01', 'On loan'], ['E02', 'Ready']]
deep:     [['E01', 'Ready'], ['E02', 'Ready']]
```

**Surprise!** The shallow copy changed too. The shallow copy has its own outer
list, but `shallow[0]` and `original[0]` are the *same* inner list. Only the
deep copy kept the old value.

You can check this yourself with the `is` operator, which asks "are these the
exact same object?":

```python
print(shallow is original)        # False -> different outer lists
print(shallow[0] is original[0])  # True  -> same inner list!
print(deep[0] is original[0])     # False -> deep copy made a new inner list
```

So what *does* a shallow copy protect you from? Changes to the **outer**
container:

```python
original.append(["E03", "Ready"])

print("original:", original)
print("shallow: ", shallow)
```

```text
original: [['E01', 'On loan'], ['E02', 'Ready'], ['E03', 'Ready']]
shallow:  [['E01', 'On loan'], ['E02', 'Ready']]
```

Adding or removing items in `original` does not affect `shallow`, because they
are different outer lists.

## Example 2: Saving a Backup Before Making Changes

A common real-world need: save the current state so you can undo changes later.

### The buggy version (shallow copy)

```python
inventory = {
    "E01": {"name": "Laptop", "available": True},
    "E02": {"name": "Projector", "available": True},
}

backup = inventory.copy()               # shallow copy

inventory["E01"]["available"] = False   # check out the laptop

print(backup["E01"])
```

```text
{'name': 'Laptop', 'available': False}
```

The "backup" was changed. Both dictionaries point to the same inner record for
`"E01"`, so the backup is useless for undo.

### The fixed version (deep copy)

```python
import copy

inventory = {
    "E01": {"name": "Laptop", "available": True},
    "E02": {"name": "Projector", "available": True},
}

backup = copy.deepcopy(inventory)       # independent snapshot

inventory["E01"]["available"] = False   # check out the laptop

print(inventory["E01"])
print(backup["E01"])

inventory = backup                      # undo: restore the saved state
print(inventory["E01"])
```

```text
{'name': 'Laptop', 'available': False}
{'name': 'Laptop', 'available': True}
{'name': 'Laptop', 'available': True}
```

The deep copy saved the original values, so undo works.

> **Independent is not the same as read-only.** A deep copy can still be
> changed. It just won't affect, or be affected by, the original.

## When Is a Shallow Copy Enough?

If the items inside the container are **immutable**, meaning they can't be
changed in place (such as `int`, `float`, `str`, `bool`, and `tuple`s of those),
a shallow copy is all you need:

```python
names = ["E01", "E02"]
names_copy = names.copy()
names_copy[0] = "E99"

print(names, names_copy)
```

```text
['E01', 'E02'] ['E99', 'E02']
```

Here `names_copy[0] = "E99"` *replaces* an item in the new list. It does not
change a shared object, so the original is safe.

## Quick Decision Guide

1. **Do you want two names for the same data?** Use assignment: `b = a`.
2. **Is the data flat, or are the inner items immutable?** A shallow copy is
   fine: `a.copy()`, `list(a)`, `dict(a)`, `a[:]`, or `copy.copy(a)`.
3. **Does the data contain lists, dicts, sets, or objects that might change
   later?** Use `copy.deepcopy(a)`.

## Trade-offs to Keep in Mind

- **Speed and memory:** A deep copy duplicates everything, so it is slower and
  uses more memory on large data. Don't use it automatically. Use it when you
  need an independent snapshot.
- **Shared on purpose:** Sometimes sharing is what you want. For example, a
  "view" that should always show live data should not be a deep copy.

## Optional: Coming from JavaScript?

Good news: **Python and JavaScript follow the same model.** In both languages,
`b = a` on a list/array or dict/object creates a second name for the *same*
object, and a shallow copy shares the inner objects. What differs is the
syntax and a few operators that look alike but behave differently.

| Topic | Python | JavaScript |
| --- | --- | --- |
| Assignment | `b = a` makes an alias | `b = a` makes an alias (same behavior) |
| Shallow copy | `a.copy()`, `list(a)`, `a[:]`, `dict(a)` | `[...a]`, `a.slice()`, `{...o}`, `Object.assign({}, o)` |
| Deep copy | `copy.deepcopy(a)` | `structuredClone(a)` |
| Same values? | `a == b` | No built-in operator for arrays or objects |
| Same object? | `a is b` | `a === b` |
| "Constant" | No `const` keyword | `const` blocks reassigning the name, but the object can still be changed |
| `+=` on a list/array | Adds items **in place**, so aliases see the change | Joins both arrays into a **string** |

### Same bug, same fix

The backup bug from Example 2 happens in JavaScript too:

```javascript
const inventory = {
  E01: { name: "Laptop", available: true },
  E02: { name: "Projector", available: true },
};

const shallow = { ...inventory };        // shallow copy
const deep = structuredClone(inventory); // deep copy

inventory.E01.available = false;

console.log(shallow.E01);  // { name: 'Laptop', available: false }
console.log(deep.E01);     // { name: 'Laptop', available: true }
```

### Trap 1: `===` is not Python's `==`

```python
print([1, 2] == [1, 2])   # True  -> same values
print([1, 2] is [1, 2])   # False -> different objects
```

```javascript
console.log([1, 2] === [1, 2]);  // false -> different objects
```

For arrays and objects, JavaScript's `===` works like Python's `is`, not
Python's `==`.

### Trap 2: `const` does not freeze an object

```javascript
const items = ["E01"];
items.push("E02");   // allowed: changes the array itself
console.log(items);  // [ 'E01', 'E02' ]
items = [];          // TypeError: Assignment to constant variable.
```

This is the same idea as "independent is not read-only": `const` stops you
from pointing the name somewhere else, but the object can still change.

### Trap 3: `+=` means different things

```python
a = [1, 2]
b = a
a += [3]
print(b)   # [1, 2, 3] -> a was changed in place, so the alias sees it
```

```javascript
let x = [1, 2];
x += [3];
console.log(x, typeof x);  // 1,23 string
```

### Trap 4: The old JSON "deep copy" trick

Older JavaScript code often deep-copies with
`JSON.parse(JSON.stringify(obj))`. It works for plain numbers, strings, arrays,
and objects, but it quietly damages other values:

```javascript
const record = { id: "E01", due: new Date("2026-11-02"), note: undefined };
const copied = JSON.parse(JSON.stringify(record));

console.log(copied);  // { id: 'E01', due: '2026-11-02T00:00:00.000Z' }
```

The `Date` became a string, and the `note` key disappeared. Any functions
stored in the object are silently dropped too. Use `structuredClone()` instead,
which keeps the `Date` as a `Date` and keeps the `note` key.

`structuredClone()` has a limit of its own: it **cannot copy functions**. If
the object contains one, it throws a `DataCloneError` instead of quietly
leaving it out. That is still better than silent data loss, because you find
out right away.

```javascript
structuredClone({ id: "E01", label() { return "Laptop"; } });
// Throws DataCloneError
```

## Check Your Understanding

1. After `b = a.copy()`, does `b.append(5)` change `a`? Why or why not?
2. After `b = a.copy()` where `a = [[1, 2], [3, 4]]`, does `b[0].append(5)`
   change `a`? Why or why not?
3. In the [State Consistency demo](main.py), why does the `aliases` list show
   E01 as "On loan" while `snapshot` still shows "Ready to borrow"?

<details>
<summary>Answers</summary>

1. **No.** `b` is a new outer list, so adding to it doesn't touch `a`.
2. **Yes.** `b[0]` and `a[0]` are the same inner list, so changing it shows up
   in both.
3. `aliases` is a new list, but it holds the *same* record dictionaries as
   `inventory`. `snapshot` was made with `deepcopy()`, so it holds independent
   copies of those records.

</details>
