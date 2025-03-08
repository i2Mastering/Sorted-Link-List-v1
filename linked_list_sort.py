"""
Linked List Sorting and Management System

This Python module reads numerical data from a file, sorts it using Merge Sort within a linked list structure, and allows user interaction to modify the list.

Features:
- Reads numerical data from `data.txt` and stores it in a linked list.
- Implements Merge Sort for sorting linked list elements.
- Provides functions to append, delete, and insert nodes in the linked list.
- Offers a user interface for adding or removing values dynamically.

Classes:
    - Node: Represents a node in a linked list.
    - LinkedList: Implements linked list operations and sorting.

Example Usage:
    ```python
    python linked_list_sort.py
    ```
    Output:
    ```
    Sorted Linked List is:
    2.5 5.6 10.3 15.8 ...
    ```

Author: Ike Iloegbu
License: MIT
"""

import sys

# Read data from file and store in sorted order
with open('data.txt', 'r') as f:
    a = [float(line.strip()) for line in f]
    a.sort()

class Node:
    """Represents a single node in a linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """Implements linked list operations and sorting using Merge Sort."""
    def __init__(self):
        self.head = None
    
    def append(self, new_value):
        """Appends a new node to the end of the linked list."""
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
        curr_node.next = new_node
    
    def deleteNode(self, key):
        """Deletes a node from the linked list by value."""
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        temp = None
    
    def sortedMerge(self, a, b):
        """Merges two sorted linked lists."""
        if not a:
            return b
        if not b:
            return a
        if a.data <= b.data:
            result = a
            result.next = self.sortedMerge(a.next, b)
        else:
            result = b
            result.next = self.sortedMerge(a, b.next)
        return result
    
    def mergeSort(self, h):
        """Sorts the linked list using Merge Sort."""
        if not h or not h.next:
            return h
        middle = self.getMiddle(h)
        next_to_middle = middle.next
        middle.next = None
        left = self.mergeSort(h)
        right = self.mergeSort(next_to_middle)
        return self.sortedMerge(left, right)
    
    def getMiddle(self, head):
        """Finds the middle node of the linked list."""
        if not head:
            return head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def printList(self):
        """Prints the linked list values."""
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

if __name__ == '__main__':
    li = LinkedList()
    for num in a:
        li.append(num)
    li.head = li.mergeSort(li.head)
    print("Sorted Linked List is:")
    li.printList()
    
    def userValues():
        """Allows users to add or remove values from the linked list interactively."""
        x = float(input("Please insert a value into the linked list: "))
        temp = li.head
        values = []
        while temp:
            values.append(temp.data)
            temp = temp.next
        
        if x in values:
            print("Value found. Removing from list.")
            li.deleteNode(x)
        else:
            print("Value not found. Adding to list.")
            li.append(x)
            li.head = li.mergeSort(li.head)
        
        print("Updated Sorted Linked List:")
        li.printList()
        userContinued()
    
    def userContinued():
        """Prompts the user to continue modifying the list or exit the program."""
        print("Would you like to continue? 1. Yes 2. No: ")
        user_choice = int(input())
        if user_choice == 1:
            userValues()
        elif user_choice == 2:
            print("Thank you! Have a great day!")
            sys.exit()
        else:
            print("Invalid choice, try again.")
            userContinued()
    
    userValues()