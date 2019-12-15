import pydoc


class Help:
    def __call__(self, obj=None):
        if obj:
            pydoc.help(obj)
        else:
            return str(self)

    def __str__(self):
        return "Usage: help(object)"

    def __repr__(self):
        return str(self)
