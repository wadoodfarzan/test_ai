try:
    1 / 0  # This will cause a ZeroDivisionError
except ZeroDivisionError as e:
    raise ValueError("Invalid operation while processing")
