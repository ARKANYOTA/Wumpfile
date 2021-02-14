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
        iconbox = Gtk.EventBox()
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
        grid.attach(box, 4, 1, 2, 2)

        # TEXT TEST
        boxFileCont = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        label2 = Gtk.Label(label="FILE CONT")
        boxFileCont.add(label2)
        boxFileCont.override_background_color(Gtk.StateType.NORMAL, Gdk.RGBA(.9,.5,.5,.5))
        grid.attach(boxFileCont, 6, 1, 16, 15)


        scrolled = Gtk.ScrolledWindow()
        scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        # FLEXBOX

        scrolled = Gtk.ScrolledWindow()
        flowbox = Gtk.FlowBox()
        flowbox.set_valign(Gtk.Align.START)
        flowbox.set_max_children_per_line(30)
        flowbox.set_selection_mode(Gtk.SelectionMode.NONE)
        self.create_flowbox(flowbox)
        scrolled.add(flowbox)

        grid.attach(scrolled, 6,1,16,15)
        # GRID OPTIONS
        grid.height = 16
        grid.width = 22
        self.add(grid)
        # ---------
        # GRID END
        # ---------
        
        # SHOW
        self.paintable()
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
    def create_flowbox(self, flowbox):
        colors = [
            "AliceBlue",
            "AntiqueWhite",
            "AntiqueWhite1",
            "AntiqueWhite2",
            "AntiqueWhite3",
            "AntiqueWhite4",
            "aqua",
            "aquamarine",
            "aquamarine1",
            "aquamarine2",
            "aquamarine3",
            "aquamarine4",
            "azure",
            "azure1",
            "azure2",
            "azure3",
            "azure4",
            "beige",
            "bisque",
            "bisque1",
            "bisque2",
            "bisque3",
            "bisque4",
            "black",
            "BlanchedAlmond",
            "blue",
            "blue1",
            "blue2",
            "blue3",
            "blue4",
            "BlueViolet",
            "brown",
            "brown1",
            "brown2",
            "brown3",
            "brown4",
            "burlywood",
            "burlywood1",
            "burlywood2",
            "burlywood3",
            "burlywood4",
            "CadetBlue",
            "CadetBlue1",
            "CadetBlue2",
            "CadetBlue3",
            "CadetBlue4",
            "chartreuse",
            "chartreuse1",
            "chartreuse2",
            "chartreuse3",
            "chartreuse4",
            "chocolate",
            "chocolate1",
            "chocolate2",
            "chocolate3",
            "chocolate4",
            "coral",
            "coral1",
            "coral2",
            "coral3",
            "coral4",
        ]

        for color in colors:
            button = self.color_swatch_new(color)
            flowbox.add(button)
    def color_swatch_new(self, str_color):
        rgba = Gdk.RGBA()
        rgba.parse(str_color)

        button = Gtk.Button()

        area = Gtk.DrawingArea()
        area.set_size_request(24, 24)
        area.connect("draw", self.on_draw, {"color": rgba})

        button.add(area)

        return button
    def on_draw(self, widget, cr, data):
        context = widget.get_style_context()

        width = widget.get_allocated_width()
        height = widget.get_allocated_height()
        Gtk.render_background(context, cr, 0, 0, width, height)

        r, g, b, a = data["color"]
        cr.set_source_rgba(r, g, b, a)
        cr.rectangle(0, 0, width, height)
        cr.fill()



TransparentWindow()
Gtk.main()
