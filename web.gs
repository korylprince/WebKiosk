[indent=4]
// valac --pkg gtk+-3.0 --pkg webkitgtk-3.0 web.gs

uses
    Gtk
    WebKit

class ValaBrowser : Window 

    webview: WebView
    button: ToolButton

    init 
        window_position = WindowPosition.CENTER
        set_default_size(1024, 768)
        create_widgets()
        connect_signals ()
        webview.grab_focus ()
        var settings = new WebSettings()
        settings.set("enable-default-context-menu",false)
        webview.set_settings(settings) 

    def create_widgets () : void
        var toolbar = new Toolbar ()
        toolbar.set_style(ToolbarStyle.BOTH)
        toolbar.get_style_context().add_class(STYLE_CLASS_PRIMARY_TOOLBAR)
        this.button = new ToolButton(null,"Refresh")
        toolbar.add (this.button)
        this.webview = new WebView ()
        var vbox = new Box (Orientation.VERTICAL, 0)
        vbox.pack_start (toolbar, false, true, 0)
        vbox.pack_start(webview,true,true,0)
        add (vbox)
    

    def connect_signals () : void
        this.destroy.connect (Gtk.main_quit)
        this.button.clicked.connect (this.start)
        this.webview.document_load_finished.connect(this.loaded)
    

    def start () : void
        show_all ()
        //URL to show
        this.webview.open ("https://google.com")
    
    
    def loaded () : void
        //Use the next command to run some javascript on page load
        //this.webview.execute_script("$('body').show()")
        return
    

    def main (arg: array of string[]) : int
        Gtk.init (ref arg)
        var browser = new ValaBrowser ()
        browser.start ()
        Gtk.main ()
        return 0
