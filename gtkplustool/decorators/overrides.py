# -*- coding: utf-8 -*-
from functools import wraps

__author__ = 'xiaolong'

# # This version works and is the general case, when using additional parameters
# def overrides(interface_class):
#     def my_decorator(method):
#         assert (method.__name__ in dir(interface_class)), \
#             'Trying to override a method named ' + \
#             method.__name__ + \
#             ' in the interface ' + \
#             interface_class.__name__ + \
#             ', which does not exist in the interface. Is this a method naming issue?'
#
#         @functools.wraps(method)
#         def wrapped(*args, **kwargs):
#             return method(*args, **kwargs)
#
#         return wrapped
#
#     return my_decorator

def overrides(interface_class):
    # print('InterfaceClass:', interface_class.__name__)
    """
    Found and added according to the following Stackoverflow post, where it is explained:
    http://stackoverflow.com/a/8313042/1829329
    Also read this:
    http://thecodeship.com/patterns/guide-to-python-function-decorators/

    - The @decorator_name() notation is equivalent to:
      decorator_name(decorated_function_name)(decorated_function_parameters)

    - The outer function needs the interface_class as a parameter, so that the inner function can read-access this class
    - The outer function receives the arguments/parameters, which are enclosed within the brackets of the decoration,
      for example:
        @decorator_name(parameters) <-- these parameters will be received in the outer function
        def function_which_is_decorated():
            ...

    - The inner function is the replacement, for the function, which is decorated and will be returned.
    - The inner function receives its parameters from ???
    - The decorator is only called once for each method we decorate with this decorator, when those methods are created.
    """
    @wraps
    def overrider(method):
        # print('Method name:', method.__name__)
        assert(method.__name__ in dir(interface_class))
        return method

    return overrider
