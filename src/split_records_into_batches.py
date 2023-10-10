from typing import List

from .exceptions import InvalidBatchSizeException


def _string_size_in_bytes(input_str: str, encoding: str) -> int:
    return len(input_str.encode(encoding))


def split_records_into_batches(
    records: List[str],
    maximum_record_bytes: int = 1_000_000,
    maximum_output_batch_bytes: int = 5_000_000,
    maximum_output_batch_length: int = 500,
    encoding: str = "utf-8",
) -> List[List[str]]:
    """This function takes in an array of records of variable sizes and splits
    the input into batches of records. Consider the following arguments.

    :param records: List of strings
    :param maximum_record_bytes: Maximum size of a record. Larger records will be discarded.
    :param maximum_output_batch_bytes: Maximum size of a single batch in bytes.
    :param maximum_output_batch_length: Maximum length of a single batch.
    :param encoding: Encoding with which the input strings are treated.

    :return: List of batches, batched according to the given options.

    PLEASE NOTE: The assignment mentioned values for suitable batch sizes and lengths,
    but I decided to make them function arguments. However, I set the values
    mentioned in the assignment as default values for the keyword arguments,
    which may not be justified if the function were actually to be packaged
    into a library. In that case, I would probably leave the keyword arguments
    undefined altogether and make them positional arguments. This way, the
    responsibility for defining the right arguments would fall on the application
    using the library.
    """

    if maximum_record_bytes > maximum_output_batch_bytes:
        raise InvalidBatchSizeException(
            "Maximum output batch size cannot be smaller than maximum record size"
        )

    output_batches = []
    current_batch: List[str] = []
    current_batch_size = 0

    for record in records:
        record_size = _string_size_in_bytes(record, encoding)

        # CASE: Maximum record size exceeded
        # > Skip record
        if record_size > maximum_record_bytes:
            continue

        max_length_exceeded = len(current_batch) >= maximum_output_batch_length
        max_bytes_exceeded = (
            current_batch_size + record_size > maximum_output_batch_bytes
        )

        # CASE: Limits exceeded
        # > Create a new batch
        if max_length_exceeded or max_bytes_exceeded:
            output_batches.append(current_batch)
            current_batch = []
            current_batch_size = 0

        # Update current batch & batch size
        current_batch += [record]
        current_batch_size += record_size

    # Append last batch only if it's not empty
    if len(current_batch) > 0:
        output_batches.append(current_batch)

    return output_batches
