class NumberAccountValueError(Exception):
    def __init__(self, message=None):
        super().__init__(message)


class NumberCardValueError(Exception):
    def __init__(self, message=None):
        super().__init__(message)
