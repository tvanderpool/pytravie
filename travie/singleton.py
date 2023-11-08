# import functools
# def singleton(cls):
#     instance = None
#     @functools.wraps(cls)
#     def getinstance():
#         if not instance:
#             instance = cls()
#         return instance
#     return getinstance

class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(
                                cls, *args, **kwargs)
        return cls._instance