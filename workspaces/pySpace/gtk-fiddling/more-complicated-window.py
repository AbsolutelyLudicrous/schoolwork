#https://python-gtk-3-tutorial.readthedocs.io/en/latest/introduction.html

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):

	def __init__(self):
		Gtk.Window.__init__(self, title="Window titlebar")

		self.button = Gtk.Button(label="Click Here")
		self.button.connect("clicked", self.on_button_clicked)
		self.add(self.button)

	def on_button_clicked(self, widget):
		print("Hello World")
		#gtk_window_set_default_size (self, 180, 180)
		#TODO make the button resize the window

win = MyWindow()	#make our new window

win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
