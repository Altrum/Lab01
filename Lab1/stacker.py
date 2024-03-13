class Stacker:
    """
    Stacker class is a class that creates an object stack to store elements in an ADT which is
    base on an array the function implemented below are: is_empty, is_full, pop, size, push, peek.
    """

    def __init__(self, max_height: int = None):
        """
        Initializes a stack object with an optional maximum height constraint.

        :args:
            max_height (int, optional): The maximum number of items the stack can hold. Defaults to None.
        """
        self._max_height = max_height
        self._items = []

    def is_empty(self):
        """
        Checks if the stack is empty.

        :returns:
            bool: True if the stack is empty, False otherwise.
        """
        return not self._items

    def is_full(self):
        """
        Checks if the stack is full if an only if the max_height has a set value.

        :returns:
            bool: True if the stack is full, False otherwise.
        """
        return self._max_height is not None and len(self._items) >= self._max_height

    def pop(self):
        """
        Removes and returns the top item from the stack.

        :returns:
            Any: The top item of the stack.

        :raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._items.pop()

    def peek(self):
        """
        Returns the top item from the stack without removing it from the stack.

        :returns:
            Any: The top item of the stack.

        :raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._items[-1]

    def push(self, item):
        """
        Pushes an item onto the stack.

        :arg:
            item (Any): The item to be pushed onto the stack.

        :raises:
            OverflowError: If the stack is full.
        """
        if self.is_full():
            raise OverflowError("Stack Overflow")
        self._items.append(item)

    def size(self):
        """
        Gets the number of items in the stack.

        :returns:
            :int: The number of items in the stack.
        """
        return len(self._items)
