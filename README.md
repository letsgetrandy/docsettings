docsettings
===========

Document your project settings with inline comments.


DocSettings reads the python module specified on the command line and looks
for comments directly preceding assignments. Comments preceding the assignment
become the documentation of that setting. Any non-comment resets the comment
text.


## TODO
So far, this is just a proof-of-concept, which just spits out the output to
STDOUT.

Plans include:
* support for variations based on environment
* generation of HTML documentation
* support for other filetypes/languages
