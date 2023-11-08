class memoized_classproperty:

    def __init__( self, fget, doc=None ):
        self.fget = fget
        self.__doc__ = doc or fget.__doc__
        self.__name__ = fget.__name__

    def __get__( self, instance, owner ):
        setattr( owner, self.__name__, result := self.fget( owner ) )
        return result
