def safe_print_integer(value):
    try:
        print("{:d}\n".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
