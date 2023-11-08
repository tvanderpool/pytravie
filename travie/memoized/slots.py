class MemoizedSlots:
    """Apply memoized items to an object using a __getattr__ scheme.

    This allows the functionality of memoized_property and
    memoized_instancemethod to be available to a class using __slots__.

    """

    __slots__ = ()

    def _fallback_getattr( self, key ):
        raise AttributeError( key )

    def __getattr__( self, key ):
        if key.startswith( "_memoized" ):
            raise AttributeError( key )
        elif hasattr( self, "_memoized_attr_%s" % key ):
            value = getattr( self, "_memoized_attr_%s" % key )()
            setattr( self, key, value )
            return value
        elif hasattr( self, "_memoized_method_%s" % key ):
            fn = getattr( self, "_memoized_method_%s" % key )

            def oneshot( *args, **kw ):
                result = fn( *args, **kw )

                def memo( *a, **kw ):
                    return result

                memo.__name__ = fn.__name__
                memo.__doc__ = fn.__doc__
                setattr( self, key, memo )
                return result

            oneshot.__doc__ = fn.__doc__
            return oneshot
        else:
            return self._fallback_getattr( key )
