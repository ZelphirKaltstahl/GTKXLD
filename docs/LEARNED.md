#Learned

## GTK+ Borders

Borders are apparently created, by wrapping a **_Gtk.Frame_** around a widget. How it's done exactly I don't know yet. Someone on Stackoverflow mentioned, that CSS could be used for that.

## GTK+ Alignment

One can align GTK+ Widgets by wrapping a **_Gtk.Alignment_** around them. The constructor signature is the following:

Gtk.Alignment(xalign=..., yalign=..., xscale=..., yscale=...)

## Signal Handling

Widgets can be connected to signals, so that they call a callback function with optional data, when they receive the signal. This can be done like this:

handler_id = widget.connect(GTKSignal.CLICKED, callback, data)

The widget can be disconnected from the signal either by using the handler_id, or the callback:

widget.disconnect(GTKSignal.CLICKED)
widget.disconnect(handler_id)

There is also a method available for checking, whether a widget is connected to a signal or not:

if not self.button.handler_is_connected(self.button_handler_id): ...

## Widget Properties

Buttons don't have an angle property, they probably cannot be rotated.
Labels can be rotated.

## How to get a list of existing/displayed Gtk Windows?

http://stackoverflow.com/a/16703307/1829329