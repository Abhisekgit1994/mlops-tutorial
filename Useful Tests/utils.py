def str_to_bool(val):

    true_vals = ['yes', 'y', '']
    false_vals = ['no', 'n']

    try:
        val = val.lower()
    except AttributeError:
        val = str(val).lower()

    if val in true_vals:
        return True
    elif val in false_vals:
        return False
    else:
        raise ValueError("Invalid input value: %s" % val)


def str_to_int(string):
    err_msg = f"Unable to convert to integer: {str(string)}"
    try:
        integer = float(string.replace(',','.'))
    except AttributeError:
        if isinstance(string, (int, float)):
            integer = string
        else:
            raise RuntimeError(err_msg)
    except (TypeError, ValueError):
        raise RuntimeError(err_msg)

    return int(integer)