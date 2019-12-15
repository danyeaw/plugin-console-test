import pydoc
import sys

from gi.repository import Gdk, GLib, Gtk, Pango

if __name__ == "__main__":
    import gi

    gi.require_version("Gtk", "3.0")


banner = (
    """Gaphor Interactive Python Console
%s
Type "help" for more information.
"""
    % sys.version
)


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

    def key_event(widget, event):
        if (
            event.keyval == Gdk.KEY_d
            and event.get_state() & Gdk.ModifierType.CONTROL_MASK
        ):
            destroy()
        return False

    w.connect("destroy", destroy)

    w.add_events(Gdk.EventMask.KEY_PRESS_MASK)
    w.connect("key_press_event", key_event)
    w.show_all()

    if main_loop:
        Gtk.main()


if __name__ == "__main__":
    main()
