import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from plugin.console import Help


def test_help():
     help = Help()

     assert help() == "Usage: help(object)"
