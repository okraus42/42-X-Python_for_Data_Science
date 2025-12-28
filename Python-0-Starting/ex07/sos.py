import sys


# Morse code dictionary
NESTED_MORSE = {
    "A": ".- ",
    "B": "-... ",
    "C": "-.-. ",
    "D": "-.. ",
    "E": ". ",
    "F": "..-. ",
    "G": "--. ",
    "H": ".... ",
    "I": ".. ",
    "J": ".--- ",
    "K": "-.- ",
    "L": ".-.. ",
    "M": "-- ",
    "N": "-. ",
    "O": "--- ",
    "P": ".--. ",
    "Q": "--.- ",
    "R": ".-. ",
    "S": "... ",
    "T": "- ",
    "U": "..- ",
    "V": "...- ",
    "W": ".-- ",
    "X": "-..- ",
    "Y": "-.-- ",
    "Z": "--.. ",
    "0": "----- ",
    "1": ".---- ",
    "2": "..--- ",
    "3": "...-- ",
    "4": "....- ",
    "5": "..... ",
    "6": "-.... ",
    "7": "--... ",
    "8": "---.. ",
    "9": "----. ",
    " ": "/ "
}


def main():
    """
    Accepts a single string argument and converts it to Morse code.
    Only alphanumeric characters and spaces are allowed.
    """
    try:
        if len(sys.argv) != 2:
            raise AssertionError("please provide a single argument.")

        text = sys.argv[1]

        # Ensure only alphanumeric + spaces
        if not all(c.isalnum() or c.isspace() for c in text):
            raise AssertionError("only alphanumeric characters and spaces\
 are allowed.")

        # Convert to uppercase and encode
        morse = ''.join(NESTED_MORSE[c.upper()] for c in text)
        # Strip trailing space if any
        print(morse.strip())

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
