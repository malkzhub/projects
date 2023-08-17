try:
    raise RuntimeWarning('Something could go wrong')
except RuntimeWarning as e: # as e is optional
    # handle the exception here
    print('nothing')

# ignoring the error

print('----------')
print()

# old
try:
    raise Exception(100)
except Exception: pass

print('----------')
print()


# new

from contextlib import suppress

def ignore_error(exception: Exception):
    """
    Use three quotes for docstrings or long strings
    """

    # : for type hinting (in a dynamic typed langage!) and
    # yes you can pass exceptions and functions as parameters
    with suppress(exception):
        raise exception('800')
        print('not printed')

ignore_error(RuntimeError)
print('this gets printed')