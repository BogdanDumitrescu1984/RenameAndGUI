# RenameAndGUI

Python script that iterates through a folder tree, reads all file names with certain extensions and changes the name of the files.
The text appended is composed of several elements 
- externally created element, added through the GUI, 
- element taken from parent folder name 
- element taken from a dictionary based on previous element

Script also prints the name of all files that can not be renamed as the new name is longer than a certain cap (256 char).

GUI element for easier use of other people.
