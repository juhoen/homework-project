class SplitToBatchesException(Exception):
    """General exception class"""


class InvalidBatchSizeException(SplitToBatchesException):
    """Will be raised if the given batch size is invalid"""
