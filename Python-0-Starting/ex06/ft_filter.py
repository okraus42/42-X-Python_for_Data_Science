def ft_filter(func, iterable):
    """ft_filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.
    """
    for item in iterable:
        if (func(item) if func else item):
            yield item
