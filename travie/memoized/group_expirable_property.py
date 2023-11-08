from .property import memoized_property
from .instancemethod import memoized_instancemethod

class group_expirable_memoized_property:
    """A family of @memoized_properties that can be expired in tandem."""

    def __init__( self, attributes=() ):
        self.attributes = []
        if attributes:
            self.attributes.extend( attributes )

    def expire_instance( self, instance ):
        """Expire all memoized properties for *instance*."""
        stash = instance.__dict__
        for attribute in self.attributes:
            stash.pop( attribute, None )

    def __call__( self, fn ):
        self.attributes.append( fn.__name__ )
        return memoized_property( fn )

    def method( self, fn ):
        self.attributes.append( fn.__name__ )
        return memoized_instancemethod( fn )
