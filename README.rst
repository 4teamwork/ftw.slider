Introduction
============

This product let you create a simple slideshow, using `slick <http://kenwheeler.github.io/slick>`_.

In each slider-pane you can define:

- An image
- HTML text
- A link

If `ftw.contentpage <http://github.com/4teamwork/ftw.contentpage>`_ is installed there will be registered a new view for the `ListingBlock` displaying images in a carousel.
See last screenshot.



Installation
============


- Add ``ftw.slider`` to your buildout configuration:

::

    [instance]
    eggs +=
        ftw.slider

- Run `bin/buildout`

- Install the generic import profile.


Compatibility
-------------

Runs with `Plone <http://www.plone.org/>`_ `4.3`.

How to use ftw.slider
=====================

If you want to display a slideshow on your content, just create a `ftw.slider.Container` and add some `ftw.slider.Pane`.

There is a viewlet which checks your content for a slider-container and displays its containing panes.


Screenshots
===========

Using ftw.slider with default plone:

.. image:: https://github.com/4teamwork/ftw.slider/raw/master/docs/screenshot_default.png

The slideshow is responsive (here OneGovBox as example):

.. image:: https://github.com/4teamwork/ftw.slider/raw/master/docs/screenshot_onegov.png

The `ftw.contentpage` carousel block with default plone:

.. image:: https://github.com/4teamwork/ftw.slider/raw/master/docs/screenshot_listingblock_plone.png

Links
=====

- Github: https://github.com/4teamwork/ftw.slider
- Issues: https://github.com/4teamwork/ftw.slider/issues
- Pypi: http://pypi.python.org/pypi/ftw.slider
- Continuous integration: https://jenkins.4teamwork.ch/search?q=ftw.slider


Copyright
=========

This package is copyright by `4teamwork <http://www.4teamwork.ch/>`_.

``ftw.slider`` is licensed under GNU General Public License, version 2.
