def slice_me(family: list, start: int, end: int) -> list:
    """ a function that takes as parameters a 2D array, prints its shape,
        and returns a truncated version of the array based on the provided
        start and end arguments."""

    try:
        # Check if family is a list
        if not isinstance(family, list):
            raise TypeError("Input must be a list of lists")

        # Check if all elements are lists and have the same length
        if not all(isinstance(row, list) for row in family):
            raise TypeError("All elements of the family must be lists")

        row_lengths = [len(row) for row in family]
        if len(set(row_lengths)) != 1:
            raise ValueError("All inner lists must have the same length")

        # Print original shape
        rows = len(family)
        cols = row_lengths[0]
        print(f"My shape is : ({rows}, {cols})")

        # Slice the list
        truncated = family[start:end]

        # Print new shape
        new_rows = len(truncated)
        print(f"My new shape is : ({new_rows}, {cols})")
    except Exception as e:
        print(f"Error: {e}")
        exit()
    return truncated
