from Lab1.error_invalid_expression import ErrorInvalidExpression
from Lab1.stacker import Stacker


# Enhancement Class turns prefix expressions to infix.
class InfixConverter:
    """
    The infix converter class functions as an enhancement for this project this class takes an expression that
    is prefix and converts it into an infix expression it has methods to check for validity and of infix and postfix,
    is_operator to check for operators at conversion for prefix to infix.
    """

    def __init__(self, expression):
        """
        Initializes an InfixConverter object with the given expression.

        Args:
            expression (str): The expression to be converted to infix notation.
        """
        self._expression = expression
        self._right_stack = Stacker()
        self._stack_operand = Stacker()
        self._temp_stack = Stacker()
        self._check_operands = Stacker()

    def is_operator(self, char) -> bool:
        """
        Checks if a character is an operator. it also checks if the carot ^ is in the expression
        and replaces $ as an exponent.

        Args:
            char (str): The character to be checked.

        Returns:
            bool: True if the character is an operator, False otherwise.
        """
        if char == '^':
            return True
        return char in ['+', '-', '*', '/', '$']

    def reverse(self):
        """
        Checks if the expression is in postfix notation.
        """
        self.is_postfix()

    def is_infix(self):
        """
        Checks if the expression is in infix notation.

        Returns:
            bool: True if the expression is in infix notation.

        Raises:
            ErrorInvalidExpression: If the expression is not in infix notation.
        """
        # Get the first Item in the expression
        for char in self._expression:
            if not char.isspace():
                self._check_operands.push(char)
                # break out of the loop
                break
        first_item = self._check_operands.peek()
        print(first_item)

        # Get the rest of the items in the expression
        # push them into a stack
        for char in self._expression:
            if not char.isspace():
                self._temp_stack.push(char)
        last_item = self._temp_stack.peek()

        #     check if  items are opends
        if first_item.isalpha() and last_item.isalpha():
            return True
        else:
            raise ErrorInvalidExpression("This is Not an Infix Expression")

    def is_postfix(self):
        """
        Checks if the expression is in postfix notation.

        Returns:
            bool: True if the expression is not in postfix notation.

        Raises:
            ErrorInvalidExpression: If the expression is in postfix notation.
        """
        # First check for postfix.
        for char in self._expression:
            if not char.isspace():
                self._right_stack.push(char)
        stack_last_item = self._right_stack.peek()
        if self.is_operator(stack_last_item):
            raise ErrorInvalidExpression("This expression is a Postfix Expression")
        else:
            return True

    def to_infix(self):
        """
        Converts the expression to infix notation.

        Returns:
            str: The expression in infix notation.

        Raises:
            ErrorInvalidExpression: If the expression is found to be an incorrect Prefix Expression.
        """
        # iterate the stack until is empty
        while not self._right_stack.is_empty():
            popped_item = self._right_stack.pop()
            # if the item is alphabetic or numeric
            if popped_item.isalpha() or popped_item.isnumeric():
                # read right to left and push alphabetic or numeric into operand stack
                self._stack_operand.push(popped_item)
            elif self.is_operator(popped_item):
                operand1 = self._stack_operand.pop()
                if self._stack_operand.is_empty():
                    raise ErrorInvalidExpression("This is an incorrect Prefix Expression")
                operand2 = self._stack_operand.pop()

                partial_infix = '(' + operand1 + popped_item + operand2 + ')'
                self._stack_operand.push(partial_infix)

        infix_expression = self._stack_operand.pop()
        return infix_expression
