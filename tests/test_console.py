import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from plugin.console import get_four
import faulthandler


faulthandler.enable()

def test_equal():
    assert get_four() == 4
