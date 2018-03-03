"""
Template for daily coding
"""
import pykata.kpis

def kata():
    __import__('pykata.kpis')
    print("abs(-1) = {0}".format(abs(-1)))
    print("any([1, True, None]) = {0}".format(any([1, True, None])))
    print("all([1, True, None]) = {0}".format(all([1, True, None])))
    print("min([1, 0, -20, 21]) = {0}".format(min([1, 0, -20, 21])))
    print("max([1, 0, -20, 21]) = {0}".format(max([1, 0, -20, 21])))
    print("Defining: class Test: pass")
    class Test: pass 
    t = Test()
    print("t = Test()")    
    print("setattr(t, 'msg', 'Hello message')")
    setattr(t, 'msg', 'Hello message')
    print("getattr(t, 'msg') = {0}".format(getattr(t, 'msg')))
    d1 = dict(a = 1, b=2)
    print("d1 = dict(a = 1, b=2) = {0}".format(d1))
    l1 = list()
    print("l1 = list() = {0}".format(l1))
    print("divmod(5, 2) = {0}".format(divmod(5, 2)))
    print("chr(65) = {0}".format(chr(65)))
    print("ord('A') = {0}".format(ord('A')))
    print("len([1, 3, 4]) = {0}".format(len([1, 3, 4])))
    print("bytearray([1, 3, 4]) = {0}".format(bytearray([1, 3, 4])))
    print("bool(None) = {0}".format(bool(None)))
    print("int('12') = {0}".format(int('12')))
    
    

def retro():
    print("Recalled {0} builtins from {1}".format(16, pykata.kpis.TOTAL_BUILTINS))