There is a difference between the internet and the web.

The internet is the system of connected computers that runs on the TCP/IP protocol stack.

It was developed in the 1960s-1980s by the US Department of Defense. [^1]

The web is the system by which computers request and share documents of a certain format, called "webpages", on the internet.

It was developed by Tim Berners-Lee in the 1990s. [^2]

We often talk about the web in metaphors of "going somewhere": surfing the web, visiting a webpage, and so on.

This belies what is actually going on. 

Your computer does not "go" to a website.

It sends a request to a server, and the server sends back a response containing the webpage's source code.

Your computer then runs that code, creating the graphical, interactive interface of a webpage that you see in your browser.






"""

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

"""

"""

INTRODUCTION

We should think about some of the very basics of what a crawler might do, 
to establish a basic functionality before enhancing usability,
customizable features, etc.

"""

"""

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


"""

"""

That means that "crawling" is more like looking inside any given webpage for URLs
it has, and then also requesting their page source.

That means that a very basic crawler should:

- Know where to begin from (i.e., at least one URL to request first)
- Be able to parse or extract URLs from the source code of pages it receives

In addition, we usually crawl for a purpose, like, we are looking
for certain kinds of information, or we want to start an index,
like a catalog, about the web, or we are basically ingesting
lots of data we want to save.

Sometimes you might do some kind of targeted crawling,
seeking something very specific.

A lot of the time, crawling is more like "trawling":
you are scraping up a ton of data on the internet
and saving it somewhere so that later, when you
have a question about something (like, which webpages exist
matching a certain description, which is what search engines do),
you already have tons of data about the web efficiently collocated. 
This can also be called "broad crawling".

It's arguably sort of a "space-time tradeoff" - you might not be sure
if a targeted crawler can efficiently find something you are looking for
in the moment you decide you want it. Broad crawling is inefficient, in 
a different way: you are saving a massive pile of data in storage,
perhaps much of the time not knowing what you might need it for,
or what's even in it.

It's sort of like the preemptive approach vs. the intentional approach, or something.

That is why two other aspects of crawling we will discuss, in a bit, are:

- what we actually do with the page source: are we trying to extract interesting data from it?
Are we trying to save that data in an organized and persistent database, 
for longterm use?

and

- crawling strategy. The web is huge. I don't know the exact numbers off 
the top of my head. But naturally, we are going to have to choose not only
which links we want to visit at all, but also in what order.
We are spelunking: we are exploring around all kinds of various paths,
walking through this door, then that door. We don't know
which door will take us to the best places we want to go. So
we have to include some sort of algorithmic logic to decide,
of all the links we could crawl next, which ones we will.

"""

"""


Arguably, crawling is a big deal. In the sense of, it is an extremely
useful operation. It is essentially the primary way anybody harvests
data from the internet. Google Search is built on crawling. All
the big AI companies that had to train their large language models
on extremely large datasets of natural language text used crawlers
to soak up as much data, webpages, texts, information, etc., 
from the web as possible. Nowadays, it is said that "data is the new oil".
There are powerful algorithms and programs that can turn data into actionable 
insights, for all kinds of reasons, from business strategy to personal need
to scientific research to political mass manipulation 
to international warfare (yes, seriously!). Acquiring data is powerful,
because knowledge really is power. 

This is why, when we crawl, we will also have to learn a lot about
the legal and ethical frameworks that exist which guide us 
in how we can crawl responsibly.

Therefore, yet another reason to learn how to do this is
simply to become more aware: the internet is a vast repository
of information, and some of it people may not realize is still out
there about them. Understanding how to thoroughly harvest data from
the web can help you become more aware that if you don't learn to
cover your tracks (i.e., practicing better data privacy strategies),
people are likely doing this to you: information about you is in 
their databases, and it can be hard to know who has it
and what they might want to do with it.


"""


"""

MAKING REQUESTS

I said that we are going to do a lot of this from scratch. I might
implement that later. Realizing it would take a while,
we will actually import some standard libraries.

"""

import requests


"""

As stated previously, we need to decide a place to begin crawling.

It would seem natural to choose some arbitrary, famous websites,
like Google, say. However, we will later see that some sites
are harder to crawl than others, and in fact, some sites
try very hard to block what they detect as automatic page interaction,
so called "bots".

You could also wonder if there is some location on the web
that is more connected to the rest of the web, so if we start there,
we would more efficiently travel to other important parts of the web.

I will suggest 2 approaches, but you can choose your own.

I think Wikipedia could be a good place to start, since it is a catalogue
of information and has many links across the web,
many of which could be high-quality and contain useful
information themselves.

My other preferred approach is to not resort to human subjectivity
to choose a place to crawl, but to explore what kinds of interesting
and obscure web pages we could discover by randomly enumerating
well-formed URLs.

We'll explore both of these approaches, starting with the latter, and falling
back on some cherry-picked URLs like Wikipedia if that doesn't work out.


"""


"""
ENUMERATING URLS

Python comes with built-in tools that make enumerating well-formed strings easy.

We are not going to enumerate every single possible URL for now,
since it would be a very large search space.

We might instead later build a tool that is a bit smarter in
choosing which URLs to try to enumerate.


"""



"""
By the RFC 1123 spec, a domain name comprises:

- letters (a-z - case insensitive)
- numbers (digits 0-9)
- the hyphen symbol "-"

A url cannot start or end with a hyphen.

We will only enumerate the domains of length 4,
and only use URLs of the form
"https://[domain].com".


"""

"""

We can construct such well-formed strings using
recursive functions.

First, we import the character sets we want to use:

"""
import string
import itertools

def enumerate_valid_strings(length=4):
    """
    Generate all valid strings where:
    - First and last char: letter or digit (a-z, 0-9)
    - Middle chars: letter, digit, or hyphen (a-z, 0-9, -)
    """
    edge_chars = string.ascii_lowercase + string.digits  # a-z, 0-9
    middle_chars = edge_chars + '-'  # a-z, 0-9, hyphen
    
    if length == 1:
        for c in edge_chars:
            yield c
    elif length == 2:
        for first in edge_chars:
            for last in edge_chars:
                yield first + last
    else:
        # General case: first + middle chars + last
        for first in edge_chars:
            for middle in itertools.product(middle_chars, repeat=length-2):
                for last in edge_chars:
                    yield first + ''.join(middle) + last

# Test it
count = 0
for s in enumerate_valid_strings(length=4):
    print(s)
    count += 1
    if count >= 20:  # Just show first 20
        break

print(f"\nTotal possible 4-char strings: {(36 * 37**2 * 36):,}")



"""


work in progress, to be conitneuds
"""



[^1]: https://en.wikipedia.org/wiki/ARPANET
[^2]: https://en.wikipedia.org/wiki/Tim_Berners-Lee
