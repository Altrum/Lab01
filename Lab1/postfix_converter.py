from Lab1.stacker import Stacker
from Lab1.error_invalid_expression import ErrorInvalidExpression


class PostfixConverter:
    """
    Class PostfixConverter

    Manages expressions in order to turn them into a postfix expression
    it takes several methods: is_operator, reverse, is_postfix, to_postfix
    """

    def __init__(self, expression):
        """
        Initializes a PostfixConverter object with the given expression.

        Args:
            expression (str): The expression to be converted to postfix notation.
        """
        self._expression = expression
        self._stack_right = Stacker()
        self._stack_operand = Stacker()
        self._postfix_check_stack = Stacker()

    # The char is supposed to read whatever char is read from the expression
    # Check is a character is an operator
    @staticmethod
    def is_operator(char) -> bool:
        """
        Checks if a character is an operator. It also checks if there is a carot ^ character
        and replaces $ as an exponent

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
         Checks if the expression is in postfix notation by reversing the expression
         inside a stack.
         """
        self.is_postfix()

    def is_postfix(self):
        """
        Checks if the expression is in postfix notation.

        Raises:
            ErrorInvalidExpression: If the expression is found to be in postfix notation.

        Returns:
            bool: True if the expression is not in postfix notation.
        """
        # First check for postfix.
        for char in self._expression:
            if not char.isspace():
                self._stack_right.push(char)
        stack_last_item = self._stack_right.peek()
        if self.is_operator(stack_last_item):
            raise ErrorInvalidExpression("This expression is a Postfix Expression")
        else:
            return True

    def to_postfix(self):
        """
        Converts the expression to postfix notation.
        it takes prefix and turns it into postfix.

        Returns:
            str: The expression in postfix notation.

        Raises:
            ErrorInvalidExpression: If the expression is found to be incorrect Prefix Expression.
        """
        # iterate the stack until is empty
        while not self._stack_right.is_empty():
            popped_item = self._stack_right.pop()
            # if the stack is alphabetic or numeric
            if popped_item.isalpha() or popped_item.isnumeric():
                # read right to left and push alpha into new stack
                self._stack_operand.push(popped_item)
            # otherwise if the character is an operator
            elif self.is_operator(popped_item):
                # save the popped item in operand1 variable
                operand1 = self._stack_operand.pop()
                # if the stack is empty
                if self._stack_operand.is_empty():
                    # Error this expression by raisin ErrorInvalid Expression
                    raise ErrorInvalidExpression("This is an incorrect Prefix Expression")
                operand2 = self._stack_operand.pop()
                # save each of the expression by concatenating them and saving them into a variable
                partial_postfix = operand1 + operand2 + popped_item
                self._stack_operand.push(partial_postfix)

        postfix_expression = self._stack_operand.pop()
        return postfix_expression
