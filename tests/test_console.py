import gi

gi.require_version("Gdk", "3.0")
gi.require_version("Gtk", "3.0")
from gi.repository import Gdk, Gtk

from plugin.console import GTKInterpreterConsole, Help, main


def test_help():
     help = Help()

     assert help() == "Usage: help(object)"


