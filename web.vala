// valac --pkg gtk+-3.0 --pkg webkitgtk-3.0 web.vala

using Gtk;
using WebKit;

public class ValaBrowser : Window {

    private WebView webview;
    private ToolButton button;
    private Spinner spinner;

    public ValaBrowser () {
        window_position = WindowPosition.CENTER;
        set_default_size(1024, 768);
        create_widgets();
        connect_signals ();
        this.webview.grab_focus ();
        var settings = new WebSettings();
        settings.set("enable-default-context-menu",false);
        webview.set_settings(settings);
    }

    private void create_widgets () {
        var toolbar = new Toolbar ();
        toolbar.set_style(ToolbarStyle.BOTH);
        toolbar.get_style_context().add_class(STYLE_CLASS_PRIMARY_TOOLBAR);
        this.button = new ToolButton(null,"Refresh");
        toolbar.add (this.button);
        this.webview = new WebView ();
        this.spinner =  new Spinner();
        this.spinner.set_margin_left(5);
        this.spinner.set_margin_right(5);
        this.spinner.set_margin_bottom(5);
        this.spinner.set_margin_top(5);
        this.spinner.start();
        var fixed = new Fixed();
        fixed.add(this.spinner);
        fixed.set_halign(Align.START);
        fixed.set_valign(Align.END);
        var overlay = new Overlay();
        overlay.add(this.webview);
        overlay.add_overlay(fixed);
        var vbox = new Box (Orientation.VERTICAL, 0);
        vbox.pack_start (toolbar, false, true, 0);
        vbox.pack_start(overlay,true,true,0);
        add (vbox);
    }

    private void connect_signals () {
        this.destroy.connect (Gtk.main_quit);
        this.button.clicked.connect (this.start);
        this.webview.document_load_finished.connect(this.loaded);
        this.webview.load_started.connect(this.started);
    }

    public void start () {
        show_all ();
        // load this url 
        this.webview.open ("https://google.com");
    }

    private void loaded () {
        this.spinner.hide();
        //Load this javascript on page load
        //this.webview.execute_script("$('body').show()");
    }

    private void started () {
        show_all();
    }

    public static int main (string[] args) {
        Gtk.init (ref args);

        var browser = new ValaBrowser ();
        browser.start ();

        Gtk.main ();

        return 0;
    }
}
