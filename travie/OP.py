import operator

__all__ = ['OP']

class _OP(object):
    def __init__(self, op, parent, asstrfmt, *asstr_args):
        self.op = op
        self.parent = parent
        self.asstr = asstrfmt.format(parent=(self.parent.asstr if self.parent else ''), *asstr_args)

    def __call__(self, *args, **kwargs):
        # print self.op, self.parent, args, kwargs
        if self.parent is not None and self.parent.op is not None:
            # print 'return self.op(self.parent'
            return self.op(self.parent(*args,**kwargs))
        # print 'return self.op'
        if self.op is not None:
            return self.op(*args, **kwargs)
        if len(args) == 1:
            return args[0]
        return args

    # def call(self, *args, **kwargs):
    #     def _call(): return self(*args, **kwargs)
    #     return _OP(_call, self, '{parent}(args,kwargs)')

    def call(self, *wargs, **wkwargs):
        def _call(method): return method(*wargs, **wkwargs)
        return _OP(_call, self, '{parent}(args,kwargs)')

    # def wrap(self, wrapfn, *wargs, **wkwargs):
    #     def w(*args, **kwargs): return wrapfn(self(*args, **kwargs), *wargs, **wkwargs)
    #     w.__name__ = wrapfn.__name__
    #     return _OP(w, self, '{}({parent})', wrapfn.__name__)

    def wrap(self, wrapfn, *wargs, **wkwargs):
        def w(val): return wrapfn(val, *wargs, **wkwargs)
        w.__name__ = wrapfn.__name__
        return _OP(w, self, '{}({parent})', wrapfn.__name__)

    # def str(self, *args, **kwargs):
    #     return self.wrap(str, *args, **kwargs)

    # def int(self, *args, **kwargs):
    #     return self.wrap(int, *args, **kwargs)

    # def float(self, *args, **kwargs):
    #     return self.wrap(float, *args, **kwargs)

    # def list(self, *args, **kwargs):
    #     return self.wrap(list, *args, **kwargs)

    # def tuple(self, *args, **kwargs):
    #     return self.wrap(tuple, *args, **kwargs)

    # def len(self, *args, **kwargs):
    #     return self.wrap(len, *args, **kwargs)

    def __getattr__(self, key):
        return _OP(operator.attrgetter(key), self, '{parent}.{}', key)

    def __getitem__(self, key):
        return _OP(operator.itemgetter(key), self, '{parent}[{}]', key)

    def __repr__(self):
        return self.asstr

    def __add__(self, other):
        def add(v): return v + other
        return _OP(add, self, '{parent} + ({!r})', other)
    def __radd__(self, other):
        def radd(v): return other + v
        return _OP(radd, self, '({!r}) + {parent}', other)
    def __sub__(self, other):
        def sub(v): return v - other
        return _OP(sub, self,'{parent} - ({!r})', other)
    def __rsub__(self, other):
        def rsub(v): return other - v
        return _OP(rsub, self, '({!r}) - {parent}', other)
    def __invert__(self):
        def _not(v): return not v
        return _OP(_not, self, 'not({parent})')
    # def __int__(self):
    #     def _int(v): return int(v)
    #     return _OP(_int, self, 'int({parent})')
    # def __long__(self):
    #     def _long(v): return long(v)
    #     return _OP(_long, self, 'long({parent})')
    # def __float__(self):
    #     def _float(v): return float(v)
    #     return _OP(_float, self, 'float({parent})')
    def __lt__(self, other):
        def lt(v): return v < other
        return _OP(lt, self, '{parent} < ({!r})', other)
    def __le__(self, other):
        def le(v): return v <= other
        return _OP(le, self, '{parent} <= ({!r})', other)
    def __eq__(self, other):
        def eq(v): return v == other
        return _OP(eq, self, '{parent} == ({!r})', other)
    def __ne__(self, other):
        def ne(v): return v != other
        return _OP(ne, self, '{parent} != ({!r})', other)
    def __gt__(self, other):
        def gt(v): return v > other
        return _OP(gt, self, '{parent} > ({!r})', other)
    def __ge__(self, other):
        def ge(v): return v >= other
        return _OP(ge, self, '{parent} >= ({!r})', other)


OP=_OP(None, None, 'OP')
