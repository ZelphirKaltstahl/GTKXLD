# Ideas

* add a menu "Dictionary" which contains actions for dictionaries, for example "add attribute" which adds an attribute to all vocables of the dictionary or search result and fills in a value specified by the user OR put it as a submenu of **_Edit_**

# Necessary

* implement a XML vocable file reader, which uses the XSD file for vocables
* change the structure of the XSD file, so that each attribute is a pair of <key> and <value>, so that the model can be easily extended
* implement a way of creating the Gtk.ListStore for the list of vocables

## TreeView
* add tooltips for the cells, which show the complete content of a cell
* add a way of copying a cell and/or a row

# Tests

* There are lots of tests to be written.

## Existence
* Is there a big character box?
* Is there a vocable treeview?
* Are there the Tabs "Dictionary" and "Training" and ...?

## Files
* test if the saved settings file contains the same as the settings file when it was loaded (String comparison).
* test if you can change a setting and it'll be saved, by loading that file again and checking if the changed value is still changed.
* make save and load testable, by giving the file paths as parameters, so that you can create test settings files
* same goes for the vocable files
* fail these tests if the xml became invalid