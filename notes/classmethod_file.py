# What is different between @stacticmethod and @classmethod

class A(object):

    def foo(self, x):
        print(f"excuting foo {self}, {x}")

    @classmethod
    def foo_class(cls, x):
        print(f"excuting foo_class {cls}, {x}")

    @staticmethod
    def foo_stactic(x):
        print(f"excuting foo_stactic {x}")

a = A()

# An usual way an object calls a method, the object a, is implicitly passed to first arg
a.foo(1)
# With class, the class of object instance is implicity passed as the first args instead of self
A.foo_class(1)
a.foo_class(1)

# With staticmethods, no one passed to . Behave like a plain function.
A.foo_stactic(1)
a.foo_stactic(1)