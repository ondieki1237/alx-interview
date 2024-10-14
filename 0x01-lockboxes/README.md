# 0x01. Lockboxes

## Description
This project focuses on solving a problem where you are given `n` locked boxes numbered from `0` to `n - 1`. Each box may contain keys to unlock other boxes, and the goal is to determine if all boxes can be opened starting from box `0`, which is initially unlocked.

The solution is implemented in Python, using key concepts such as list manipulation, graph traversal, and recursion.

## Requirements
- **Editor**: vi, vim, emacs
- **Operating System**: Ubuntu 20.04 LTS
- **Language**: Python 3.4.3
- All files should end with a new line.
- The first line of each file should start with `#!/usr/bin/python3`.
- Code must follow the PEP 8 style guide (version 1.7.x).
- All files must be executable.

## Project Tasks

### 0. Lockboxes
Write a method that determines if all the boxes can be opened.

- **Prototype**: `def canUnlockAll(boxes)`
- `boxes` is a list of lists where each sublist contains keys to other boxes.
- A key with the same number as a box opens that box.
- You can assume that all keys are positive integers.
- Return `True` if all boxes can be opened, otherwise return `False`.

### Example

```python
boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes)) # True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes)) # True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes)) # False

