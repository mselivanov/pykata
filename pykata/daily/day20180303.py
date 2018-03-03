"""
Template for daily coding
"""
import pykata.kpis

class NoDirMethod(object):
    def __init__(self, message):
        self.message = message
    
    def __getattr__(self):
        print("In __getattr__")
        return super().__getattr__(self)

class DirMethod(object):
    def __init__(self, message):
        self.message = message
    
    def __dir__(self):
        return [name for name in self.__dict__.keys() if not name.startswith('__')]

class Root(object):
    @classmethod
    def sing(cls, song):
        print("Root singing: {0}".format(song))
        
    def say(self, message):
        print("In Root: {0}".format(message))

class ChildLevel1Number1(Root):
    @classmethod
    def sing(cls, song):
        print("ChildLevel1Number1 singing: {0}".format(song))
        super().sing(song)

    def say(self, message):
        print("In ChildLevel1Number1: {0}".format(message))
        super().say(message)

class ChildLevel1Number2(Root):
    @classmethod
    def sing(cls, song):
        print("ChildLevel1Number2 singing: {0}".format(song))
        super().sing(song)

    def say(self, message):
        print("In ChildLevel1Number2: {0}".format(message))
        super().say(message)

class ChildLevel2Number1(ChildLevel1Number1, ChildLevel1Number2):
    @classmethod
    def sing(cls, song):
        print("ChildLevel2Number1 singing: {0}".format(song))
        super().sing(song)

    def say(self, message):
        print("In ChildLevel2Number1: {0}".format(message))
        super().say(message)

class ChildLevel2Number2(ChildLevel1Number2, ChildLevel1Number1):
    @classmethod
    def sing(cls, song):
        print("ChildLevel2Number2 singing: {0}".format(song))
        super().sing(song)

    def say(self, message):
        print("In ChildLevel2Number2: {0}".format(message))
        super().say(message)

class ChildLevel2Number3(ChildLevel1Number2, ChildLevel1Number1):
    @classmethod
    def sing(cls, song):
        print("ChildLevel2Number3 singing: {0}".format(song))
        super(ChildLevel1Number2, ChildLevel2Number3).sing(song)

    def say(self, message):
        print("In ChildLevel2Number3: {0}".format(message))
        super(ChildLevel1Number2, self).say(message)
        
        
def kata():
    ndm = NoDirMethod("Hi, there")
    print("dir(NoDirMethod('Hi, there')) = {0}".format(dir(ndm)))
    dm = DirMethod("Hello!")
    print("dir(DirMethod('Hello!')) = {0}".format(dir(dm)))
    c1 = ChildLevel2Number1()
    c1.say("Child 1 says")
    c2 = ChildLevel2Number2()
    c2.say("Child 2 says")
    c3 = ChildLevel2Number3()
    c3.say("Child 3 says")
    ChildLevel2Number1.sing("Song of wind")
    ChildLevel2Number2.sing("Song of earth")
    ChildLevel2Number3.sing("Song of fire")
    
def retro():
    print("Recalled dir() method")
    print("Recalled super() method")