from rlcompleter import Completer


class Help:
    def __call__(self):
        return str(self)

    def __str__(self):
        return "Usage: help(object)"
