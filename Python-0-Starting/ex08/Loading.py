import os


def ft_tqdm(lst: range):
    """
Simple tqdm-like progress bar using yield.
Only imports os. Updates bar in-place using print.

Args:
    lst: An iterable (usually range) to wrap.
Yields:
    Items from the iterable one by one.
    """
    total = len(lst)
    for i, item in enumerate(lst, 1):
        yield item

        # Get terminal width (fallback to 80 if fails)
        try:
            width = os.get_terminal_size().columns
        except OSError:
            width = 80

        bar_length = min(40, width - 30)  # leave space for percentage/counter

        # Progress calculation
        percent = i / total
        filled = int(bar_length * percent)
        empty = bar_length - filled

        # Build bar string
        bar = '#' * filled + '-' * empty

        # Print in-place
        print(f'\r[{bar}] {percent*100:6.2f}% ({i}/{total})',
              end='',
              flush=True)

    print()  # newline at the end
