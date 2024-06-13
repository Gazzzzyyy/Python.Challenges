"""
Write a function that takes a string and a width as input. It should chop the string into new lines that are
left justified. Each line should be exactly w characters long.
"""


def left_justify(text: str, w: int) -> str:
    """
    Takes a string and formats it into left-justified text with each line exactly 'w' characters long.

    Args:
    text (str): The input string which could be one or more sentences.
    w (int): The width of each line.

    Returns:
    str: The left-justified text with each line exactly 'w' characters long.
    """
    words = text.split()
    lines = []
    current_line = []

    for word in words:
        # Check if adding the next word would exceed the width
        if sum(len(w) for w in current_line) + len(current_line) + len(word) > w:
            # If yes, justify the current line and add it to lines
            lines.append(justify_line(current_line, w))
            current_line = [word]
        else:
            # Otherwise, add the word to the current line
            current_line.append(word)

    # Justify the last line and add it to lines
    if current_line:
        lines.append(justify_line(current_line, w))

    return "\n".join(lines)


def justify_line(words: list, w: int) -> str:
    """
    Justifies a line to be exactly 'w' characters long.

    Args:
    words (list): List of words to justify.
    w (int): The width of the line.

    Returns:
    str: A left-justified line of exactly 'w' characters.
    """
    line = ' '.join(words)
    extra_spaces = w - len(line)

    if len(words) == 1:
        # If the line has only one word, pad with spaces at the end
        return words[0] + ' ' * extra_spaces

    # Distribute the extra spaces between words
    gaps = len(words) - 1
    spaces_per_gap = extra_spaces // gaps
    extra = extra_spaces % gaps

    justified_line = ""
    for i, word in enumerate(words[:-1]):
        justified_line += word + ' ' * (spaces_per_gap + 1)
        if i < extra:
            justified_line += ' '
    justified_line += words[-1]

    return justified_line

if __name__ == "__main__":


    # Example usage
    text = "This is an example of text that needs to be left justified."
    width = 20
    print(left_justify(text, width))
