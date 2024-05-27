"""
You have an array of student records. Each record is a string containing a student's name followed by their score. You need to reorder the records so that:

Students are sorted by their scores in descending order.
If two students have the same score, they should be sorted by their names in ascending order.
Return the final order of the student records.
"""

from typing import List, Tuple, Any


def sort_student_records(records: List[str]) -> List[str]:

    def sorting_function(record: str) -> Tuple[Any]:

        first_name, last_name, score = record.split(" ")
        name = f"{first_name} {last_name}"
        return (-int(score), name)

    records.sort(key=sorting_function)

    return records


if __name__ == "__main__":

    def test_sort_student_records():
        test_cases = [
            {
                "input": [
                    "Willy Wonka 100",
                    "Alice Alfie 85",
                    "Bob Bridget 92",
                    "Charlie Charles 85",
                    "David Davidson 100",
                    "Eve Evangelista 92",
                ],
                "expected": [
                    "David Davidson 100",
                    "Willy Wonka 100",
                    "Bob Bridget 92",
                    "Eve Evangelista 92",
                    "Alice Alfie 85",
                    "Charlie Charles 85",
                ],
            },
            {
                "input": [
                    "John Doe 50",
                    "Jane Smith 75",
                    "Alice Johnson 75",
                    "Zara Zee 90",
                ],
                "expected": [
                    "Zara Zee 90",
                    "Alice Johnson 75",
                    "Jane Smith 75",
                    "John Doe 50",
                ],
            },
            {
                "input": [
                    "Anna Adams 99",
                    "Bella Brown 99",
                    "Chris Clarke 100",
                ],
                "expected": [
                    "Chris Clarke 100",
                    "Anna Adams 99",
                    "Bella Brown 99",
                ],
            },
            {
                "input": [
                    "Emma Emerson 60",
                    "Noah Nelson 80",
                    "Liam Lucas 80",
                    "Olivia Olson 60",
                ],
                "expected": [
                    "Liam Lucas 80",
                    "Noah Nelson 80",
                    "Emma Emerson 60",
                    "Olivia Olson 60",
                ],
            },
            {
                "input": [
                    "Abe Abel 90",
                    "Sam Samson 100",
                    "Eve Edison 90",
                    "Ivy Ives 100",
                ],
                "expected": [
                    "Ivy Ives 100",
                    "Sam Samson 100",
                    "Abe Abel 90",
                    "Eve Edison 90",
                ],
            },
        ]

        for i, case in enumerate(test_cases):
            result = sort_student_records(case["input"])
            assert (
                result == case["expected"]
            ), f"Test case {i + 1} failed: {result} != {case['expected']}"

        print("All test cases passed!")

    test_sort_student_records()
