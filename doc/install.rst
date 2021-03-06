Install
=======

.. important::

   This package requires Python3 and isn't compatible with Python2.

Below you will find instructions to install perprof-py for any operation system
that run Python and after that more detail instructions for some popular
operation system.

General
-------

Install perprof-py in a Python environment with pip is easy::

    # pip install -r REQUIREMENTS
    # python setup.py install

.. note::

   You can `install it locally
   <https://docs.python.org/3.3/install/index.html#alternate-installation-the-home-scheme>`_
   if you want but to take advantage of bash
   completion we recomend you to install it globablly.

.. note::

   For developers you can use `the develop mode
   <http://pythonhosted.org/setuptools/setuptools.html#develop-deploy-the-project-source-in-development-mode>`_
   instead. ::

    # python setup.py develop

To see a demo::

    $ perprof --mp -o demo -f --demo

GNU/Linux Distribution
----------------------

The general instructions probably work for you if you already using Python3 as
default.  Instructions for distributions that still using Python2 are found
below.

Debian
~~~~~~
::

    # apt-get install python3 pip3

And follow the general instructions replacing ``python`` with ``python3`` and
``pip`` with ``pip3``.

Ubuntu
~~~~~~
::

    # apt-get install python3 pip3

And follow the general instructions replacing ``python`` with ``python3`` and
``pip`` with ``pip3``.

Fedora
~~~~~~

::

    # yum install python3 pip3

And follow the general instructions replacing ``python`` with ``python3`` and
``pip`` with ``pip3``.

Arch
~~~~

::

    # pacman -S pip

And follow the general instructions.

Gentoo
~~~~~~

::

    # emerge pip

And follow the general instructions.

Mac OS X
--------

.. note::

   Comming soon.

Windows
-------

.. note::

   Comming soon.
