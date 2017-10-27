import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):

	def __init__(self):
		Gtk.Window.__init__(self, title="Hello World")

		self.box = Gtk.Box(spacing=6)	# buffer of 6 pixels
		self.add(self.box)

		self.button1 = Gtk.Button(label="Hello")
		self.button1.connect("clicked", self.on_button1_clicked)
		self.box.pack_start(self.button1, True, True, 0)

		self.button2 = Gtk.Button(label="Goodbye")
		self.button2.connect("clicked", self.on_button2_clicked)
		self.box.pack_start(self.button2, True, True, 0)

	def on_button1_clicked(self, widget):
		print("Hello")

	def on_button2_clicked(self, widget):
		otherwin.show_all()

class aDifferentKindOfWindow(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title="Check me out!")

		self.containerbox=Gtk.Box(spacing=100)
		self.add(self.containerbox)

win = MyWindow()
otherwin=MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()

newwin=aDifferentKindOfWindow()
newwin.connect("delete-event", Gtk.main_quit)
newwin.show_all()
Gtk.main()
