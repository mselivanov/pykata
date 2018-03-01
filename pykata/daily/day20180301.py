"""
Template for daily coding
"""
import pykata.kpis

def kata():
    class Test1: pass
    
    print("abs(-1) = {0}".format(abs(-1)))
    print("divmod(5, 2) = {0}".format(divmod(5, 2)))
    print("max([2, 3, 4, 0, 10]) = {0}".format(max([2, 3, 4, 0, 10])))
    print("min([2, 3, 4, 0, 10]) = {0}".format(min([2, 3, 4, 0, 10])))
    print("len([2, 3, 4, 0, 10]) = {0}".format(len([2, 3, 4, 0, 10])))
    print("len('Hello!') = {0}".format(len('Hello!')))
    print("class Test1: pass")
    setattr(Test1, 'a', 'Hello')
    print("setattr(Test1, 'a', 'Hello') = {0}".format(Test1.__dict__))
    d = {'a':1}
    print("getattr(d, '__doc__') = {0}".format(getattr(d, '__doc__')))
    print("dict(a=1, b=2) = {0}".format(dict(a=1, b=2)))
    print("list((1, 4, 5)) = {0}".format(list((1, 4, 5))))
    print("set([1, 1, 1, 2, 2]) = {0}".format(set([1, 1, 1, 2, 2])))
    print("frozenset([1, 1, 1, 2, 2]) = {0}".format(frozenset([1, 1, 1, 2, 2])))
    
    
def retro():
    print("Recalled {0} builtins from {1}".format(11, pykata.kpis.TOTAL_BUILTINS))