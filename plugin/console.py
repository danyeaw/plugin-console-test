import pydoc
from rlcompleter import Completer

from gi.repository import Gdk, Gtk

if __name__ == "__main__":
    import gi

    gi.require_version("Gtk", "3.0")


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


def main(main_loop=True):
    w = Gtk.Window()

    def destroy(arg=None):
        Gtk.main_quit()

    w.connect("destroy", destroy)
    w.show_all()

    if main_loop:
        Gtk.main()


if __name__ == "__main__":
    main()
