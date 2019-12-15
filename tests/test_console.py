from plugin.console import Help


# class KeyEvent:
#    def __init__(self, keyval, state=0):
#        self.keyval = keyval
#        self.state = state


def test_help():
     help = Help()

     assert help() == "Usage: help(object)"

