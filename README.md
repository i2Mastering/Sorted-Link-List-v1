# Linked List Sorting and Management System

## Description
This Python program reads numerical data from a file, sorts it using Merge Sort within a linked list structure, and allows user interaction to modify the list dynamically. It provides essential linked list operations such as insertion, deletion, and sorting.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Example Output](#example-output)
- [Classes](#classes)
- [Requirements](#requirements)
- [License](#license)

## Features
- Reads numerical data from `data.txt` and stores it in a linked list.
- Implements Merge Sort for sorting linked list elements.
- Provides functions to append, delete, and insert nodes in the linked list.
- Offers a user interface for adding or removing values dynamically.

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/linked-list-sort.git
   ```
2. Navigate to the project directory:
   ```sh
   cd linked-list-sort
   ```
3. Ensure Python 3.x is installed.

## Usage
1. Prepare a file named `data.txt` containing numerical values, one per line.
2. Run the script:
   ```sh
   python linked_list_sort.py
   ```
3. The program will:
   - Read data from `data.txt`.
   - Store the numbers in a linked list.
   - Sort the list using Merge Sort.
   - Display the sorted linked list.
   - Allow users to add or remove values interactively.

## Example Output
```sh
Sorted Linked List is:
2.5 5.6 10.3 15.8 ...

Please insert a value into the linked list: 7.5
Value not found. Adding to list.
Updated Sorted Linked List:
2.5 5.6 7.5 10.3 15.8 ...
Would you like to continue? 1. Yes 2. No:
```

## Classes
### `Node`
- Represents a single node in a linked list.
- **Attributes:** `data`, `next` (pointer to next node).

### `LinkedList`
- Implements linked list operations and sorting using Merge Sort.
- **Methods:**
  - `append(new_value)`: Adds a node to the linked list.
  - `deleteNode(key)`: Removes a node by value.
  - `sortedMerge(a, b)`: Merges two sorted linked lists.
  - `mergeSort(h)`: Sorts the linked list using Merge Sort.
  - `getMiddle(head)`: Finds the middle node for Merge Sort.
  - `printList()`: Prints the linked list.

## Requirements
- Python 3.x

## License
This project is licensed under the MIT License.
