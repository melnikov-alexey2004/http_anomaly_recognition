# Все примеры на Python 3!

def add_this(f):
    def wrapped(self, *args, **kwargs):
        f.__globals__['this'] = self
        return f(*args, **kwargs)
    return wrapped

class C:
    name = 'Alex'

    @add_this
    # @staticmethod
    def say(phrase):
        print(C.say.__globals__)
        print("{} says: {}".format(this.name, phrase))

c = C()
c.say('Can you believe it? There is no `self` here!')