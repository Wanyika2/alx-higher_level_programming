#!/usr/bin/python3
"""
Module for MyList class.
"""


class MyList(list):
    """
    A subclass of list that adds additional functionality.

    Public Methods:
        print_sorted(self): Prints the list sorted in ascending order.
    """

    def print_sorted(self):
        """
        Prints the list sorted in ascending order.
        
        Args:
            self (MyList): The MyList object to operate on.

        Returns:
            None
        """
        sorted_list = sorted(self)
        print(sorted_list)
