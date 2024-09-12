import operator
# def _pwrap(fn):
#     pass
# def log_decorator(log_enabled):
#     def actual_decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             if log_enabled:
#                 print("Calling Function: " + func.__name__)
#             return func(*args, **kwargs)
#         return wrapper
#     return actual_decorator

# def star( method, *args):
#     args = args[:-1] + args[-1]
#     return method( *args )

def starmap( method, *args):
    args = list( args[:-1] ) + list(args[-1])
    return map( method, *args )

def contains(a, b=None):
    # a in b
    def _contains(b):
        return a in b
    return _contains if b is None else _contains(b)

def not_(method):
    from functools import wraps
    @wraps(method)
    def _not(*args, **kwargs):
        return not method(*args, **kwargs)
    return _not

def startswith(b):
    def _startswith(a): return a.startswith(b)
    return _startswith

def endswith(b):
    def _endswith(a): return a.endswith(b)
    return _endswith

def isNone(istrue=True):
    def _isNone(v):
        return (v is None) if istrue else (v is not None)
    return _isNone

def equals(a):
    def equals(b): return a == b
    return equals
eq = equals

def chain(*funcs):
    # def call(v ,f): return f(v)
    # def chain(v): return reduce(call, funcs, v)
    def chain( v ):
        for f in funcs:
            v = f(v)
        return v
    return chain

def chainmap( funcs, *args):
    return map( chain(*funcs), *args )

def itemgetter(*items):
    if len(items) == 1:
        return operator.itemgetter(items[0])
    return chain(*map(operator.itemgetter, items))
chained_itemgetter = itemgetter

def attrgetter(*items):
    if len(items) == 1 and '.' in items[0]:
        items = items[0].split('.')
    if len(items) == 1:
        return operator.attrgetter(items[0])
    return chain(*map(operator.attrgetter, items))
chained_attrgetter = attrgetter

def makeai(L):
    ai_dict = {'attr':operator.attrgetter, 'item':operator.itemgetter}
    b_dict = {n:m for n, m in L.items() if n not in ('makeai', 'starmap', 'chain','not_','chained_itemgetter','chained_attrgetter') and not n.startswith('__') and callable(m) }
    def make_chain_wrapper(a_m, b_m):
        def chain_wrapper(a, b):
            return chain(a_m(a), b_m(b))
        return chain_wrapper
    return {'{}_{}'.format(a_n, b_n):make_chain_wrapper(a_m, b_m) for a_n, a_m in ai_dict.items() for b_n, b_m in b_dict.items() }
locals().update(makeai(locals()))
del makeai
