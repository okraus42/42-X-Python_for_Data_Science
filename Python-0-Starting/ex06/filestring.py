import sys
from ft_filter import ft_filter  # Import your custom filter


def main():
    """
    Accepts a string s and an integer n.
    Prints a list of words from s with length greater than n using ft_filter.
    """
    try:
        if len(sys.argv) != 3:
            raise AssertionError("Please provide a string and an integer.")

        s = sys.argv[1]
        try:
            n = int(sys.argv[2])
        except ValueError:
            raise AssertionError("The second argument must be an integer.")

        # Use ft_filter to filter words
        filtered_words = ft_filter(lambda w: len(w) > n, s.split())

        # Convert to list (list comprehension requirement)
        result = [word for word in filtered_words]

        print(result)
        # print(filtered_words)

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
