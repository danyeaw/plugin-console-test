import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from plugin.console import get_four


def test_equal():
    assert get_four() == 4
