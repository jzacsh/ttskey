#!/usr/bin/env python

# TTS Volume Slider
#
# author: Jonathan Zacsh <jzacsh@gmail.com>
#
# Present our user with a gnome-applet, exactly like the volume-slider in
# GNOME, that allows them to change the speed of our espeak TTS utility in
# ~/bin/share/tts_xsel

#@TODO: finish reading:
# http://saravananthirumuruganathan.wordpress.com/2010/01/15/creating-gnome-panel-applets-in-python/
#@TODO: finish reading:
# http://www.znasibov.info/blog/post/gnome-applet-with-python-part-1.html

import pygtk
pygtk.require('2.0')

import gtk
import gnomeapplet

def sample_factory(applet, iid):
    label = gtk.Label("Success!")
    applet.add(label)

    applet.show_all()
    return gtk.TRUE

gnomeapplet.bonobo_factory("OAFIID:TTSKeyVolumeSlider",
                             gnomeapplet.Applet.__gtype__,
                             "hello world", "0", sample_factory)
