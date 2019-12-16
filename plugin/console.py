import gi
from rlcompleter import Completer

gi.require_version("Gtk", "3.0")
from gi.repository import Gdk, Gtk


class Help:
    def __str__(self):
        return "Usage: help(object)"


def main():
    w = Gtk.Window()
    w.show()
    w.connect("destroy", Gtk.main_quit)
    Gtk.main()


if __name__ == "__main__":
    main()
