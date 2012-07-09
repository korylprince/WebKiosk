WebKiosk

This is my attempt to create a relatively secure Kiosk environment with a Minimal Web Browser with Ubuntu, ratpoison, and a custom Gtk application.
The .py, .vala, and .gs files are the same program written in Python, Vala, and Genie respectively.

https://github.com/korylprince/WebKiosk

#Installing#

First log in to Ubuntu and set your Network and Power settings. I also recommend you install an ssh server so you can get back into the machine.

Edit the program with your language of choice to set the url, then copy the resulting program (compiling if need be) to /opt/web.
Copy com.py to /opt/, and .ratpoisonrc to your home folder.

To set up autologin, copy ratpoison.desktop to /usr/share/xsessions/ and copy lightdm.conf to /etc/lightdm/ and edit for the autologin user.

To disable the ttys when pressing Ctrl+F1-6, create files /etc/init/tty[1-6].override that contain the text "manual". (That's one file for each tty.)

This creates a fairly secure Kiosk environment, unless, of course, users have access to the power where they could get access to recovery mode with Grub. Besides that no commands cannot be run, and the computer cannot be started.

#Usage#

On reboot the computer will login and go straight to your web page.

You can set the webpage to load and an optional js script to run on each page load. com.py is a simple daemon that will restart the program if it is ended.

Pressing the Refresh button will reload the start page.

You may have a problem with the program loading before networking begins. In this case I suggest you add a timeout in com.py by adding the following code to the top:

    import time
    time.sleep(t)

Where t is the number of seconds to wait.

#Caveats#

A bug in Gtk causes the program to crash whenever the toolbar is double-clicked under certain window managers including ratpoison.

This is part of the reason for using com.py. A bug report has been filed [here](https://bugzilla.gnome.org/show_bug.cgi?id=679468).

#License#

Code is Copyright 2012 Kory Prince (korylprince at gmail dot com)
This code is Public Domain. There is no warranty. Do whatever you want. It'd be nice if you sent me an email telling me someone used it though.
If you'd like help, I can't promise anything, but there's no hurt in asking.
