Introduction
============

This product let you create a simple slideshow, using `slick <http://kenwheeler.github.io/slick>`_.

In each slider-pane you can define:

- An image
- HTML text
- A link


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

Links
=====

- Github project repository: https://github.com/4teamwork/ftw.slider
- Issue tracker: https://github.com/4teamwork/ftw.slider/issues
- Package on pypi: http://pypi.python.org/pypi/ftw.slider
- Continuous integration: https://jenkins.4teamwork.ch/search?q=ftw.slider


Copyright
=========

This package is copyright by `4teamwork <http://www.4teamwork.ch/>`_.

``ftw.slider`` is licensed under GNU General Public License, version 2.

.. image:: https://cruel-carlota.pagodabox.com/d9c95f38d2ad57caaf293a9072e1f81d
   :alt: githalytics.com
   :target: http://githalytics.com/4teamwork/ftw.slider
