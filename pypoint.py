from lambdastat import lreturn
class pvar:
    def _s_(self, o):
        self.__val__['var'] = o
    def __init__(self, value : object):
        self.__val__ = {'var': value}
        self.get = lambda : lreturn(self.__val__['var'])
        self.set = lambda obj : self._s_(obj)
class ptn:
    def _s_(self, o):
        self._va_.__val__['var'] = o
    def __init__(self, var : pvar):
        if type(var) != pvar:
            raise Exception("Variable specified is not pvar")
        self._va_ = var
        self.get = lambda : lreturn(self._va_.__val__['var'])
        self.set = lambda obj : self._s_(obj)
class pointer(ptn):
    pass