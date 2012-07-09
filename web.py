#!/usr/bin/python
from gi.repository import Gtk as gtk, WebKit as webkit

def on_quit(widget):
    gtk.main_quit()

def refreshclick(widget):
    #Open this url
    webview.open('https://google.com/')

def runscript(*args):
    #Run this script on page load
    #webview.execute_script("$('body').hide()")
    return


window = gtk.Window(type=gtk.WindowType.TOPLEVEL)
window.set_position(gtk.WindowPosition.CENTER)
window.set_default_size(1024, 768)
window.fullscreen()
window.connect("destroy", on_quit)

toolbar = gtk.Toolbar(toolbar_style=gtk.ToolbarStyle.BOTH)
context = toolbar.get_style_context()
context.add_class(gtk.STYLE_CLASS_PRIMARY_TOOLBAR)

refresh = gtk.ToolButton()
refresh.set_label('Refresh')
refresh.connect('clicked',refreshclick)
toolbar.add(refresh)

webview = webkit.WebView()
webview.props.settings.props.enable_default_context_menu = False
webview.connect('document_load_finished',runscript)
vbox = gtk.VBox()
vbox.pack_start(toolbar,False,False,0)
vbox.pack_start(webview,True,True,0)

window.add(vbox)
window.show_all()
refreshclick(webview)

gtk.main()
