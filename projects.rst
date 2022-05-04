Projects
========

:slug: projects
:type: text

Personal projects that I consider noteworthy, in some manner or other, are
described below:


gwax.(com\|net\|org)
--------------------

* Source: |github-icon| `gwax/www-gwax <https://github.com/gwax/www-gwax>`_

.. |github-icon| image:: /icons/github.svg
    :class: svg-icon

This site is one of my ongoing projects. I've been maintaining it in some
fashion since the mid 20-aughts. It's an example of various things, many not
so technically interesting. A lot of details can be found in the
`About > The site page <link://slug/about-site>`__. The interesting pieces are
likely to show up in `Blog > Categories > meta <link://category/meta>`__.


mtg-ssm
-------

* Source: |github-icon| `gwax/mtg_ssm <https://github.com/gwax/mtg_ssm>`_
* Package: |python-icon| `pypi/mtg-ssm <https://pypi.org/project/mtg-ssm/>`_

.. |python-icon| image:: /icons/python.svg
    :class: svg-icon

Magic: the Gathering Spreadsheet Manager
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Magic: the Gathering Spreadsheet Manager (mtg-ssm) for short is a command line
tool, written in `Python <https://www.python.org>`_ (3), that generates Excel
spreadsheets for use in tracking `Magic: the Gathering <http://magic.wizards.com/>`_
card collections. The tool can also update existing spreadsheets with new sets
and card information (preserving existing collection counts).

Card and set data is sourced from `MTG JSON <http://mtgjson.com/>`_.

The sheets are constructed in such a way that they can show you how many copies
of a given card exist in other sets to ease search for cards in your
collection. There are also limited import/export capabilities.

I eat my own dog food. An mtg-ssm generated spreadsheet, stored in
`Dropbox <https://www.dropbox.com/>`_, is how I manage my Magic card
collection.


GsMtgJson
---------

* Source: |github-icon| `gwax/GsMtgJson <https://github.com/gwax/GsMtgJson>`_

GsMtgJson is the ancestor of `mtg-ssm`_. It is a Google Apps Script project
that produces Google Sheets for tracking Magic collections. The project is
essentially dead at this point, having been supplanted by `mtg-ssm`_.


GwTest
------

* Source: |github-icon| `gwax/GwTest <https://github.com/gwax/GwTest>`_

While building GsMtgJson, I suffered a great deal of frustration while
debugging and refactoring my code, due to a lack of a decent way to test what
I was doing.

Solution: build a unit testing framework for Google Apps Scripts.

GwTest is a unit testing framework in the spirit of PyUnit, JUnit, and SUnit.


Novel Potentials for the Simulation of Polyethylene and other Polymeric Systems
-------------------------------------------------------------------------------

* Page: `Novel Potentials for the Simulation of Polyethylene and other Polymeric Systems <link://slug/thesis>`__

To complete my undergraduate degree in Materials Science, I had to write a
thesis. I chose to write my thesis on discrete element simulations of polymer
chains. I was quite proud of the software that I built and work that I did.
