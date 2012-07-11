#!/usr/bin/python

# This is not the more object oriented approach as the other with classes and such

from gi.repository import Gtk,WebKit

def on_quit(widget):
    Gtk.main_quit()

def refreshclick(widget):
    #Open this url
    webview.open('https://google.com/')

def runscript(*args):
    spinner.hide()
    #Run this script on page load
    #webview.execute_script("$('body').hide()")
    return

def end(*args):
    window.show_all()

window = Gtk.Window(type=Gtk.WindowType.TOPLEVEL)
window.set_position(Gtk.WindowPosition.CENTER)
window.set_default_size(1024, 768)
window.connect("destroy", on_quit)

toolbar = Gtk.Toolbar(toolbar_style=Gtk.ToolbarStyle.BOTH)
context = toolbar.get_style_context()
context.add_class(Gtk.STYLE_CLASS_PRIMARY_TOOLBAR)

refresh = Gtk.ToolButton()
refresh.set_label('Refresh')
refresh.connect('clicked',refreshclick)
toolbar.add(refresh)

webview = WebKit.WebView()
webview.props.settings.props.enable_default_context_menu = False
webview.connect('document_load_finished',runscript)
webview.connect('load_started',end)
spinner = Gtk.Spinner(margin_left=5, margin_right=5, margin_top=5, margin_bottom=5)
spinner.start()
fixed = Gtk.Fixed()
fixed.add(spinner)

fixed.set_halign(Gtk.Align.START)
fixed.set_valign(Gtk.Align.END)

overlay = Gtk.Overlay()
overlay.add(webview)
overlay.add_overlay(fixed)

vbox = Gtk.VBox()
vbox.pack_start(toolbar,False,False,0)
vbox.pack_start(overlay,True,True,0)

window.add(vbox)
window.show_all()
refreshclick(webview)

Gtk.main()
