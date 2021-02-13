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

        # CONFIG CONSTANTES
        self.BorderIcon = ConfigBorderIcon #???
        self.NombreDeFileX = ConfigNombreDeFileX
        self.NombreDeFileY = ConfigNombreDeFileY
        self.SpaceSize = ConfigSpaceSize
        self.FileSize = ConfigFileSize

        # CONFIG VARIABLES
        self.OpenPath = ConfigOpenPath
        self.FolderIcon = ConfigFolderIcon
        self.Reduced = ConfigReduced
        self.FolderIcon = ConfigFolderIcon
         
        # SET CONSTANTES
        self.Width = (self.NombreDeFileX+1)*self.FileSize+(self.NombreDeFileX+2)*self.SpaceSize
        self.Height = self.NombreDeFileY*self.FileSize+(self.NombreDeFileY+1)*self.SpaceSize
        self.set_size_request(self.Width, self.Height)
        
        # SET VARIABLES


        self.connect('destroy', Gtk.main_quit)
        # self.connect('draw', self.draw)

        # ----------
        # GRID
        # ---------
        grid = Gtk.Grid()
        # ICONBOX
        iconbox = Gtk.Box()
        iconbox.override_background_color(Gtk.StateType.NORMAL, Gdk.RGBA(.5,.5,.5,.5))
        # iconbox.set_spacing(0)
        grid.attach(iconbox, 0,0,4,4)

        # ICON
        icon = Gtk.Image() 
        icon.set_from_file(self.FolderIcon)
        grid.attach(icon,0,0,4,4)

        # QUIT BUTTON
        quit_btn = Gtk.Button(label='Quitter')
        quit_btn.connect('clicked', Gtk.main_quit)
        # grid.attach(quit_btn, 2, 1, 1, 1)

        # TEXT TEST
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        label1 = Gtk.Label(label="Test")
        box.add(label1)
        box.override_background_color(Gtk.StateType.NORMAL, Gdk.RGBA(.9,.5,.5,.5))
        grid.attach(box, 2, 1, 3, 3)

        # GRID OPTIONS
        grid.set_row_spacing(0)
        grid.set_column_spacing(0)
        self.add(grid)
        # ---------
        # GRID END
        # ---------
        
        # SHOW
        # self.paintable()
        self.show_all()

    def draw(self, widget, context):
        context.set_source_rgba(0, 0, 0, 0)
        context.set_operator(cairo.OPERATOR_SOURCE)
        context.paint()
        context.set_operator(cairo.OPERATOR_OVER)
    def paintable(self):
        screen = self.get_screen()
        visual = screen.get_rgba_visual()
        if visual and screen.is_composited():
            self.set_visual(visual)
        self.set_app_paintable(True)

TransparentWindow()
Gtk.main()
