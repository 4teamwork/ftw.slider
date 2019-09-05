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


Upgrade from 2.4.x to 3.0.x
===========================

The ``ftw.contentpage`` ListingBlock integration has been removed with the 3.0.0 release.
If you are at this point, please consider upgrading your ``ftw.contentpage`` installation to ``ftw.simplelaoyut``.
With ``ftw.simpelayout`` you can install ``ftw.sliderblock`` to get the same feature set.


Compatibility
-------------

Runs with `Plone <http://www.plone.org/>`_ `4.3` and `5.1`.

How to use ftw.slider
=====================

If you want to display a slideshow on your content, just create a `ftw.slider.Container` and add some `ftw.slider.Pane`.

There is a viewlet which checks your content for a slider-container and displays its containing panes.

Settings
--------

To ensure access4all you can use the settings `canNext` which is the option
for en/disabling the slider button to move to the next image (when set true the
button is shown, when false it is hidden), `canPrev` equivalent for the last
image button and the `arrowsOnHover` option (when true only showing the buttons
on hover, when false showing them always).

Other settings are `autoplay` (when true automatically sliding to the next
image after set time) and `autoplaySpeed` (a number for the time to wait until
sliding to the next image in milliseconds).

Those options are to be set in json format in the configuration textarea of the
ftw.slider block like:

::

    {"canNext":true, "canPrev":true, "arrowsOnHover":false}

Extended Slick configuration
============================

In addition to the default slick-configuration options you can use the following `ftw.slider` specific custom options

Random
------

Shuffles the slides on each page reload to display the slides in a random order.

::

    {"random": true}


Screenshots
===========

Using ftw.slider with default plone:

.. image:: https://github.com/4teamwork/ftw.slider/raw/master/docs/screenshot_default.png

The slideshow is responsive (here OneGovBox as example):

.. image:: https://github.com/4teamwork/ftw.slider/raw/master/docs/screenshot_onegov.png


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
