# LSGI3315 Lab 2 20016345D Example 5
# How Tuple/Dictionary passes the keyword or non-keyword arguments
def test_args_kwargs(arg1, arg2, arg3):
    print('arg1:', arg1)
    print('arg2:', arg2)
    print('arg3:', arg3)


if __name__ == '__main__':
    print('*Arguments:')
    args = ('two', 3, 5)
    test_args_kwargs(*args)
    print('**KeyWord Arguments:')
    kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
    test_args_kwargs(**kwargs)
