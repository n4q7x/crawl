

import sys

'''

The sys module is how you can interact with certain objects
which the Python interpreter itself has access to, 
particularly things like command-line arguments,
stdin, stdout, and stderr, modules,
and information about the runtime environment, 
like the operating system and Python version.
It can also be used for debugging.

In this program, we are just using it
to grab any command-line arguments the user might pass.
But in the beginning, we may not even need that.

'''

'''

We should think about some of the very basics of what a crawler might do, 
to establish a basic functionality before enhancing usability,
customizable features, etc.

'''

'''

Of course, "crawling" is a metaphor. 
We often talk about the internet / web as if we are *going* somewhere - 
visiting a webpage, surfing the internet.

But (and this will only be news if you are completely new to how the web works),
when you "visit" or "load" a webpage, actually,
your computer sends out a *request* - a little message
that travels over the internet to a *server* (a computer)
that is responsible for operating that website.

The server receives the request, which says, 
"Hello, I'd like to have your website please",
and it sends the code of the website back over the internet
to the requestor.

When your computer receives that code, it runs it, generating
the dynamic, graphical application you see inside your browser.

Therefore, in a way, "visiting a website" is kind of similar
to just opening an application you have installed on your computer,
except for the code is sent over the internet at the last minute,
your computer receives it and runs it.


'''

