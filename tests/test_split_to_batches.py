from datetime import date
from functools import partial
from unittest import TestCase

from parameterized import parameterized

from src.exceptions import InvalidBatchSizeException, SplitToBatchesException
from src.split_records_into_batches import split_records_into_batches


class TestSplitRecordsToBatches(TestCase):
    def test_invalid_batch_size_raises_exception(self):
        with self.assertRaises(InvalidBatchSizeException) as context:
            split_records_into_batches(
                [],
                maximum_record_bytes=200,
                maximum_output_batch_bytes=100,
            )

        raised_exception = context.exception
        self.assertTrue(isinstance(raised_exception, SplitToBatchesException))
        self.assertEqual(
            str(raised_exception),
            "Maximum output batch size cannot be smaller than maximum record size",
        )

    @parameterized.expand(
        [
            # Test with empty input
            (
                partial(
                    split_records_into_batches,
                    records=[],
                ),
                [],
            ),
            # Test with only invalid input (too large records)
            (
                partial(
                    split_records_into_batches,
                    records=["a" * 100] * 10,
                    maximum_record_bytes=10,
                ),
                [],
            ),
            # Test with one valid input record
            (
                partial(
                    split_records_into_batches,
                    records=["a"] + ["a" * 100] * 10,
                    maximum_record_bytes=10,
                ),
                [["a"]],
            ),
            # Test with two valid input records
            (
                partial(
                    split_records_into_batches,
                    records=["a"] + ["a" * 100] * 10 + ["b"],
                    maximum_record_bytes=1,
                    maximum_output_batch_bytes=2,
                ),
                [["a", "b"]],
            ),
            # Test with two valid input records and two batches
            (
                partial(
                    split_records_into_batches,
                    records=["a"] + ["a" * 100] * 10 + ["b"],
                    maximum_record_bytes=1,
                    maximum_output_batch_bytes=1,
                ),
                [["a"], ["b"]],
            ),
            # Test with only valid input records with small max batch length
            (
                partial(
                    split_records_into_batches,
                    records=["a"] * 10,
                    maximum_output_batch_length=3,
                ),
                [["a", "a", "a"], ["a", "a", "a"], ["a", "a", "a"], ["a"]],
            ),
        ]
    )
    def test_split_records_into_batches(self, func, expected_result):
        assert func() == expected_result
