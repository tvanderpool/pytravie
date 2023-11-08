from functools import wraps

def _generator_wrapper( real_decorator ):

    @wraps( real_decorator )
    def decorator_wrapper(*Dargs, **Dkwargs ):

        inner = real_decorator(*Dargs, **Dkwargs )

        def generator_func_wrapper( generator_func ):

            @wraps( generator_func )
            def wrapped_generator_func(*Gargs, **Gkwargs ):
                return inner( generator_func(*Gargs, **Gkwargs ) )

            return wrapped_generator_func

        return generator_func_wrapper

    return decorator_wrapper

@_generator_wrapper
def join( joinwith ):

    def inner( results ):

        return joinwith.join( results )

    return inner

lines = join( '\n' )
args = join( ', ' )

# def join(joinwith):
#     def wrapper(fn):
#         @wraps(fn)
#         def wrapped(*args,**kwargs):
#             return joinwith.join(fn(*args,**kwargs))
#         return wrapped
#     return wrapper

# def foreach(fn, *fn_args, **fn_kwargs):

# def call():
