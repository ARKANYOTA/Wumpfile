#!/usr/bin/env python

#  Copyright (c) 2017 Kurt Jacobson
#  License: https://kcj.mit-license.org/@2017

import cairo
import gi

gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')

from gi.repository import Gtk
from gi.repository import Gdk

ConfigReduced = True
ConfigFolderIcon = "/home/ay/Apps/Wumpfile/themes/kora/folder.png"
ConfigBorderIcon = "/home/ay/Apps/Wumpfile/themes/kora/border.png"
ConfigNombreDeFileX = 3
ConfigNombreDeFileY = 3
ConfigSpaceSize = 10
ConfigFileSize = 100
ConfigOpenPath = "/home/ay"

class TransparentWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="WumpFile")

        self.FolderIcon = ConfigFolderIcon
        self.BorderIcon = ConfigBorderIcon
        self.NombreDeFileX = ConfigNombreDeFileX
        self.NombreDeFileY = ConfigNombreDeFileY
        self.SpaceSize = ConfigSpaceSize
        self.FileSize = ConfigFileSize
        self.Reduced = ConfigReduced
        self.FolderIcon = ConfigFolderIcon
        self.OpenPath = ConfigOpenPath

        self.Width = (self.NombreDeFileX+1)*self.FileSize+(self.NombreDeFileX+2)*self.SpaceSize
        self.Height = self.NombreDeFileY*self.FileSize+(self.NombreDeFileY+1)*self.SpaceSize

        self.set_size_request(self.Width, self.Height)

        self.connect('destroy', Gtk.main_quit)
        self.connect('draw', self.draw)

        grid = Gtk.Grid()        
        icon = Gtk.Image() 
        icon.set_from_file(self.FolderIcon)
        grid.attach(icon, 1,0,1,1)

        border = Gtk.Image() 
        border.set_from_file(self.BorderIcon)
        grid.attach(border, 1,0,1,1)

        quit_btn = Gtk.Button(label='Quitter')
        quit_btn.connect('clicked', Gtk.main_quit)
        grid.attach(quit_btn, 1, 1, 1, 1)

        label1 = Gtk.Label(label="Test")
        sbar = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        sbar.add(label1) 
        grid.attach(sbar, 1, 2, 1, 1)

        self.add(grid)


        screen = self.get_screen()
        visual = screen.get_rgba_visual()
        if visual and screen.is_composited():
            self.set_visual(visual)
        
        self.set_app_paintable(True)
        self.show_all()

    def draw(self, widget, context):
        context.set_source_rgba(0, 0, 0, 0)
        context.set_operator(cairo.OPERATOR_SOURCE)
        context.paint()
        context.set_operator(cairo.OPERATOR_OVER)

TransparentWindow()
Gtk.main()
