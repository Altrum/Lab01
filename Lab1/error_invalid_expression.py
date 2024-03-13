class ErrorInvalidExpression(Exception):
    """
    Custom exception class for invalid expressions.

    :attributes:
        :message (str): The error message describing the invalid expression.
    """
    def __init__(self, message):
        """
        Initializes the ErrorInvalidExpression object with the provided message.

        :args:
            message (str): The error message describing the invalid expression.
        """
        super().__init__(message)
        self.message = message
