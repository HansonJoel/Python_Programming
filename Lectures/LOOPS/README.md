# Mastering Loops in Python

## 📌 Overview

This folder contains notes and examples from my tutorial on `while` loops and `for` loops in Python. Loops are essential for iteration, allowing us to execute a block of code multiple times efficiently.

## 📖 Table of Contents

- [While Loop](#while-loop)
- [For Loop](#for-loop)
- [Break and Continue Statements](#break-and-continue-statements)
- [Looping Through Data Structures](#looping-through-data-structures)
- [Nested Loops](#nested-loops)

## 🔁 While Loop

A `while` loop runs as long as a specified condition remains `True`.

```python
x = 0
while x < 5:
    print(x)
    x += 1
```

### ✅ Key Points:

- Be cautious of infinite loops by ensuring the condition eventually becomes `False`.
- The `break` statement can be used to exit the loop prematurely.

## 🔄 For Loop

A `for` loop is used for iterating over sequences (e.g., lists, tuples, strings).

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

### ✅ Key Points:

- Commonly used with the `range()` function for numerical iteration.
- Can iterate over strings, lists, tuples, sets, and dictionaries.

## 🚀 Break and Continue Statements

- **`break`** exits the loop immediately:

  ```python
  for i in range(5):
      if i == 3:
          break
      print(i)
  ```

- **`continue`** skips the rest of the current iteration and proceeds to the next:

  ```python
  for i in range(5):
      if i == 3:
          continue
      print(i)
  ```

## 📂 Looping Through Data Structures

Loops can be used to traverse lists, dictionaries, and more.

```python
person = {"name": "Alice", "age": 25}
for key, value in person.items():
    print(key, ":", value)
```

## 🔄 Nested Loops

A loop inside another loop allows for complex iteration structures.

```python
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")
```

## 🎯 Conclusion

Understanding loops is fundamental to writing efficient and readable Python code. Mastery of `while` and `for` loops, along with `break` and `continue`, is essential for handling iterations effectively.

---

## 📌 Next Steps:

- ✅ Practice by writing custom loops for different tasks.
- ✅ Experiment with list comprehensions for concise looping.
- ✅ Explore how loops interact with functions and file handling.

Happy coding! 🚀
