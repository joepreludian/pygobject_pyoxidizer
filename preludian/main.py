import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
import pathlib


def run():
    builder = Gtk.Builder()

    app_dir = pathlib.Path(__file__).parent

    builder.add_from_file(str(app_dir / 'helloGTK.glade'))

    window = Gtk.Window(title="Hello World")
    window.show()
    window.connect("destroy", Gtk.main_quit)
    Gtk.main()

if __name__ == '__main__':
    run()
