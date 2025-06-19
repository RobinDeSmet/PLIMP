class TodoNotFound(Exception):
    """Exception raised when a Todo item is not found."""

    pass


class TodoAlreadyExists(Exception):
    """Exception raised when a Todo item already exists."""

    pass
