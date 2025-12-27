import sys

try:
    if len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")
    elif len(sys.argv) < 2:
        raise AssertionError("no argument is provided")
    else:
        try:
            value = int(sys.argv[1])
            if (value % 2) == 0:
                print("I'm Even.")
            else:
                print("I'm Odd.")
        except ValueError:
            raise AssertionError("argument is not an integer")
except AssertionError as e:
    print(f"AssertionError: {e}")
