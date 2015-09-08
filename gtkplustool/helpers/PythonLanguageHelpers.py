# -*- coding: utf-8 -*-


def overrides(interface_class):
    """
    Found and added according to the following Stackoverflow post, where it is explained:
    http://stackoverflow.com/a/8313042/1829329
    Also read this:
    http://thecodeship.com/patterns/guide-to-python-function-decorators/

    - The outer function needs the interface class as a parameter, so that the inner function can read-access this class
    - The inner function is the replacement, for the function this decorator is used on
    - TODO: parameter of the inner function explanation?
    - The decorator is only called once for each method we decorate with this decorator, when those methods are created.
    """
    def overrider(method):
        print(method)
        assert(method.__name__ in dir(interface_class))
        return method
    return overrider
