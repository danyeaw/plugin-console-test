import gi

gi.require_version("Gdk", "3.0")
gi.require_version("Gtk", "3.0")
from gi.repository import Gdk, Gtk

from plugin.console import GTKInterpreterConsole, Help, main


class KeyEvent:
    def __init__(self, keyval, state=0):
        self.keyval = keyval
        self.state = state


def test_help():
     help = Help()

     assert help() == "Usage: help(object)"


