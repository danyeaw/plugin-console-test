from rlcompleter import Completer

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


def test_answer():
    assert 5 == 5