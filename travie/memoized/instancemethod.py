from functools import update_wrapper

def memoized_instancemethod( fn ):
    """Decorate a method memoize its return value.

    Best applied to no-arg methods: memoization is not sensitive to
    argument values, and will always return the same value even when
    called with different arguments.

    """

    def oneshot( self, *args, **kw ):
        result = fn( self, *args, **kw )

        def memo( *a, **kw ):
            return result

        memo.__name__ = fn.__name__
        memo.__doc__ = fn.__doc__
        self.__dict__[ fn.__name__ ] = memo
        return result

    return update_wrapper( oneshot, fn )
