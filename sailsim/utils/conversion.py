def stringToFloat(val):
    """Convert a string to int or float. Return 0 if it is NaN."""
    if val.isnumeric():
        return int(val)
    try:
        return float(val)
    except ValueError:
        return 0
