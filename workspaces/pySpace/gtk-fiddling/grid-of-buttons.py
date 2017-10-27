import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk

class MyWindow(gtk.Window):
	def __init__(self):
		gtk.Window.__init__(self, title="Generic Window Title")

win = MyWindow()				#generate the window
win.connect("delete-event", gtk.main_quit)	#needed so that the program quits when the window closes
win.show_all()
gtk.main()
