class MaximumNumberLogs(Exception):
    """Exception raised for maximum number logs in file"""

    def __init__(self, message):
        """
        :param message: explanation of the error
        """
        super().__init__()
        self.message = message

    def __str__(self):
        return f'Maximum number of logs in one logfile are {self.message}'
