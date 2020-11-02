def check_conditional_fail(conditional_value, **kwargs):
    if conditional_value:
        raise RuntimeError('Fail upon receiving value')
    return 