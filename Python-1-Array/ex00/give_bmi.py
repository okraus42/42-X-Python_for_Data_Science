def _is_number(value):
    """
    Check whether a value is an int or float (excluding bool).

    Parameters
    ----------
    value : any
        Value to check.

    Returns
    -------
    bool
        True if value is int or float (but not bool), False otherwise.
    """
    return type(value) in (int, float)


def _is_nan(value):
    """
    Check whether a value is NaN.

    Parameters
    ----------
    value : float

    Returns
    -------
    bool
        True if value is NaN, False otherwise.
    """
    return value != value


def _is_inf(value):
    """
    Check whether a value is positive or negative infinity.

    Parameters
    ----------
    value : float

    Returns
    -------
    bool
        True if value is infinite, False otherwise.
    """
    return abs(value) == float("inf")


def validate_measurements(
    height,
    weight,
    *,
    min_height=0.5,
    max_height=3.0,
    min_weight=2.0,
    max_weight=500.0,
):
    """
    Validate height and weight measurement lists.

    Checks performed:
    - height and weight have the same length
    - values are numeric (int or float)
    - no NaN or infinity values
    - values fall within user-defined ranges

    Parameters
    ----------
    height : list
        List of height values in meters.
    weight : list
        List of weight values in kilograms.
    min_height : float
        Minimum allowed height.
    max_height : float
        Maximum allowed height.
    min_weight : float
        Minimum allowed weight.
    max_weight : float
        Maximum allowed weight.

    Raises
    ------
    TypeError
        If a value is not numeric.
    ValueError
        If values are invalid, non-finite, or out of range.
    """
    if len(height) != len(weight):
        raise ValueError("height and weight must be the same length")

    for i, (h, w) in enumerate(zip(height, weight)):
        if not _is_number(h) or not _is_number(w):
            raise TypeError(f"Non-numeric value at index {i}: {h=}, {w=}")

        if _is_nan(h) or _is_nan(w):
            raise ValueError(f"NaN detected at index {i}: {h=}, {w=}")

        if _is_inf(h) or _is_inf(w):
            raise ValueError(f"Infinity detected at index {i}: {h=}, {w=}")

        if not (min_height <= h <= max_height):
            raise ValueError(f"Invalid height at index {i}: {h}")

        if not (min_weight <= w <= max_weight):
            raise ValueError(f"Invalid weight at index {i}: {w}")


def give_bmi(height, weight):
    """
    Calculate BMI values from height and weight lists.

    This function validates the input data before performing
    the calculation. If validation fails, an empty list is returned.

    Parameters
    ----------
    height : list
        Heights in meters.
    weight : list
        Weights in kilograms.

    Returns
    -------
    list
        List of BMI values, or an empty list if validation fails.
    """
    try:
        validate_measurements(height, weight)
    except (TypeError, ValueError) as exc:
        print(f"BMI calculation failed: {exc}")
        return []

    bmi = []
    for h, w in zip(height, weight):
        bmi.append(w / (h * h))
    return bmi


def apply_limit(bmi, limit):
    """
    Apply a threshold limit to BMI values.

    Parameters
    ----------
    bmi : list
        List of BMI values.
    limit : float
        Threshold value.

    Returns
    -------
    list
        List of booleans indicating whether each BMI exceeds the limit.
        Returns an empty list if input is invalid.
    """
    try:
        if not _is_number(limit):
            raise TypeError("limit must be a numeric value")

        results = []
        for i, value in enumerate(bmi):
            if not _is_number(value):
                raise TypeError(f"Non-numeric BMI value at index {i}: {value}")
            if _is_nan(value) or _is_inf(value):
                raise ValueError(f"Invalid BMI value at index {i}: {value}")

            results.append(value > limit)

        return results

    except (TypeError, ValueError) as exc:
        print(f"Limit application failed: {exc}")
        return []
