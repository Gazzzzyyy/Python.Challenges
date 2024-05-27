"""
You have an array of logs. Each log is a space-delimited string of words. For each log, the first word is an
alphanumeric identifier. Then, either:

Each word after the identifier will consist only of lowercase letters, or;
Each word after the identifier will consist only of digits.
You need to reorder the logs so that:

The letter-logs come before all digit-logs.
The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them
lexicographically by their identifiers.
The digit-logs should be put in their original order.
Return the final order of the logs.
"""

from typing import AnyStr, List


def reorder_log_files(logs: List[str]) -> List[str]:
    """
    Reorder the logs such that letter-logs come before digit-logs,
    and letter-logs are sorted lexicographically by content, then by identifier.

    Args:
    logs (List[str]): The list of log strings.

    Returns:
    List[str]: The reordered list of logs.
    """

    def get_key(log):
        identifier, rest = log.split(" ", 1)
        if rest[0].isdigit():
            return (1,)  # Digit logs are put after letter logs
        else:
            return (
                0,
                rest,
                identifier,
            )  # Letter logs are sorted by content and then identifier

    logs.sort(key=get_key)
    return logs


if __name__ == "__main__":
    print(
        reorder_log_files(
            [
                "dig1 8 1 5 1",
                "let1 art can",
                "dig2 3 6",
                "let2 own kit dig",
                "let3 art zero",
            ]
        )
    )
    # returns ["let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"]
