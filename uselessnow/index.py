import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
# config 
ConfigReduced = True

# windows
win = Gtk.Window(title="WumpFile")
win.reduced = ConfigReduced
# win.set_opacity(0.5)

wid = Gtk.Widget
wid.set_opacity(win, 0.5)
# icon
icon = Gtk.Image() 
icon.set_from_file("/home/ay/Apps/Wumpfile/folder.png")
# win.add(icon)

#affich
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()



"""

class MyWindow(Gtk.Window):
    def __init__(self):

        Gtk.Window.__init__(self, title="WumpFile")
        # widget = Gtk.Widget()
        # widget.set_opacity(0.5)
        self.set_background("f00")
        self.reduced = ConfigReduced
        icon = Gtk.Image() 
        icon.set_from_file("/home/ay/Apps/Wumpfile/folder.png")
        self.add(icon)

    def on_button_clicked(self, widget):
        print("Hello World")
        """
