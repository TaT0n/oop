from pip._vendor.msgpack.fallback import xrange


def generator(i):
    class A(object):
        def __init__(self):
            self.value = i
            pass

    return A


classes = [generator(x) for x in xrange(10)]
for x in xrange(10):
    klass = classes[x]
    print(klass().value)
