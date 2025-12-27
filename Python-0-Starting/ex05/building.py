import sys


def main():
    """
    Analyzes a string to count uppercase letters, lowercase letters, digits,
        spaces, and punctuation marks.

    Input:
    - Zero command-line arguments: the program reads a line of text from
        standard input.
    - One command-line argument: the program analyzes that argument as
        the text.
    - More than one argument: raises an AssertionError and exits.

    Output:
    Prints the total number of characters and the counts of uppercase letters,
        lowercase letters, digits, spaces, and punctuation marks
        in the provided text.
    """
    try:
        if len(sys.argv) > 2:
            raise AssertionError("Please provide at most one argument.")
        elif len(sys.argv) == 2:
            text = sys.argv[1]
        else:
            print("What is the text to count?")
            text = sys.stdin.readline()
        upper = 0
        lower = 0
        punctuation = 0
        space = 0
        digit = 0
        for char in text:
            if char.isupper():
                upper += 1
            elif char.islower():
                lower += 1
            elif char.isdigit():
                digit += 1
            elif char.isspace():
                space += 1
            elif (not char.isalnum()
                  and not char.isspace()
                  and char.isprintable()):
                punctuation += 1
        print(f"The text contains {len(text)} characters:")
        print(f"{upper} upper letters")
        print(f"{lower} lower letters")
        print(f"{punctuation} punctuation marks")
        print(f"{space} spaces")
        print(f"{digit} digits")
    except AssertionError as e:
        print(f"Assertion error: {e}")
        sys.exit(0)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
