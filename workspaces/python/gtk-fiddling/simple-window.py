#stolen from https://python-gtk-3-tutorial.readthedocs.io/en/latest/introduction.html

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

win = Gtk.Window()                          #generate the window
win.connect("delete-event", Gtk.main_quit)  #needed so that the program quits when the window closes
win.show_all()
Gtk.main()
