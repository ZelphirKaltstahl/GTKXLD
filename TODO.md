# Ideas

* add a menu "Dictionary" which contains actions for dictionaries, for example "add attribute" which adds an attribute to all vocables of the dictionary or search result and fills in a value specified by the user OR put it as a submenu of **_Edit_**

# Necessary

* implement a XML vocable file reader, which uses the XSD file for vocables
* change the structure of the XSD file, so that each attribute is a pair of <key> and <value>, so that the model can be easily extended
* implement a way of creating the Gtk.ListStore for the list of vocables

* make colmns resizeable