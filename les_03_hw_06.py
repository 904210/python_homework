def int_func(lst):
    """taking a string from small latin letters and returning it, but with a capital first letter"""

    print(' '.join(lst).title())


help(int_func)
int_func(input('input text: ').split())
