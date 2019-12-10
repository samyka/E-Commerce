Getting Started with E-Commerce Development
======================================

.. note::

   If you are planning on using E-Commerce to build your own shop,
   read the :doc:`Getting Started with E-Commerce guide <getting_started>`
   instead.

.. note::

   Interested in contributing to E-Commerce? Take a look at our `Contribution
   Guide <https://www.E-Commerce.com/en/E-Commerce/contribution-guide>`__.

Requirements
------------
* Python 2.7.9+/3.4+. https://www.python.org/download/.
* Node.js (v0.12 or above). https://nodejs.org/en/download/
* Any database supported by Django.

Installation for E-Commerce Development
----------------------------------

To start developing E-Commerce, you'll need a Git checkout of E-Commerce and a
Github fork of E-Commerce for creating pull requests.  Github pull requests
are used to get your changes into E-Commerce Base.

1. If you haven't done so already, create a fork of E-Commerce in Github by
   clicking the "Fork" button at https://github.com/E-Commerce/E-Commerce and
   clone the fork to your computer as usual. See `Github Help about
   forking repos <https://help.github.com/articles/fork-a-repo/>`__ for
   details.

2. Python < 3.6 is recommended only advanced users. To cover large amount
   of issues with setup it is recommended to run
   `pip install -U pip setuptools wheel` before creating virtualenv.

3. Setup a virtualenv and activate it.  You may use the traditional
   ``virtualenv`` command, or the newer ``python -m venv`` if you're
   using Python 3.  See `Virtualenv User Guide
   <https://virtualenv.pypa.io/en/latest/userguide.html>`__, if you
   are unfamiliar with virtualenv.  For example, following commands
   create and activate a virtualenv in Linux:

   .. code-block:: shell

      virtualenv E-Commerce-venv
      . E-Commerce-venv/bin/activate

4. Finally, you'll need to install E-Commerce in the activated virtualenv in
   development mode.  To do that, run the following commands in the
   root of the checkout (within the activated virtualenv):

   .. code-block:: shell

      pip install -e .[everything]

.. note::
    Some extra steps is required for **Windows**

    If you want to install all requirements just with pip, you have to install MS
    Visual C++ Build Tools as explained in `Python’s wiki
    <https://wiki.python.org/moin/WindowsCompilers>`__. This way
    everything will be build automatically on your Windows machine, alternatively
    you may install failed to build packages from https://www.lfd.uci.edu/~gohlke/pythonlibs/.

    If you have OSError: dlopen() failed to load a library: cairo / cairo-2 error,
    please carefully follow these `instructions
    <https://weasyprint.readthedocs.io/en/latest/install.html#windows>`__.

    If you still have the same error, be sure that your installed python and GTK run
    time has the same 32 or 64 bit. It's important.

    Error is still there? Try to edit Windows environment PATH, and move GTK Runtime
    location to the top of the list.

.. note::
    Extra information/warning regarding SQLite `read more
    <https://github.com/E-Commerce/E-Commerce/issues/1730>`__.


Workbench, the built-in test project
------------------------------------

The Workbench project in the repository is a self-contained Django
project set up to use an SQLite database. It is used by the test suite
and is also useful for development on its own.

Practically the only difference to a normal Django project is that instead
of ``python manage.py``, one uses ``python -m E-Commerce_workbench``.

To get started with Workbench, invoke the following in the E-Commerce working copy
root.

.. code-block:: shell

   # Migrate database.
   python -m E-Commerce_workbench migrate

   # Import some basic data.
   python -m E-Commerce_workbench E-Commerce_init

   # Create superuser so you can login admin panel
   python -m E-Commerce_workbench createsuperuser

   # Run the Django development server (on port 8000 by default).
   python -m E-Commerce_workbench runserver

You can use the created credentials to log in as a superuser on
http://127.0.0.1:8000/sa/ .

Building resources
------------------

E-Commerce uses JavaScript and CSS resources that are compiled using various
Node.js packages.  These resources are compiled automatically by
``setup.py`` when installing E-Commerce with pip, but if you make changes to
the source files (e.g. under ``E-Commerce/admin/static_src``), the resources
have to be rebuilt.

This can be done with

.. code-block:: shell

   python setup.py build_resources

The command also accepts couple arguments, see its help for more details:

.. code-block:: shell

   python setup.py build_resources --help

.. note::
    Make sure your running rather new version from `Node
    <https://nodejs.org/en/>`__ and non LTS version is recommended
    for advanced users only.


Running tests
-------------

To run tests in the active virtualenv:

.. code-block:: shell

   py.test -v --nomigrations E-Commerce_tests
   # Or with coverage
   py.test -vvv --nomigrations --cov E-Commerce --cov-report html E-Commerce_tests

To run tests for all supported Python versions run:

.. code-block:: shell

   pip install tox  # To install tox, needed just once
   tox

Running browser tests
---------------------

.. code-block:: shell

   E-Commerce_BROWSER_TESTS=1 py.test -v --nomigrations E-Commerce_tests/browser

Headless with Firefox:

.. code-block:: shell

   E-Commerce_BROWSER_TESTS=1 MOZ_HEADLESS=1 py.test -v --nomigrations E-Commerce_tests/browser

For Chrome

.. code-block:: shell

   E-Commerce_BROWSER_TESTS=1 py.test -v --nomigrations --splinter-webdriver=chrome E-Commerce_tests/browser


For OSX with Homebrew:

.. code-block:: shell

    # Install Chrome driver (tested with 2.34.522932 (4140ab217e1ca1bec0c4b4d1b148f3361eb3a03e))
    brew install chromedriver

    # Install Geckodriver (for Firefox)
    brew install geckodriver

    # If your current version is below 0.23.0 (for Firefox)
    brew upgrade geckodriver

    # Make sure the selenium is up to date (tested with 3.141.0)
    pip install selenium -U

    # Make sure splinter is up to date (tested with 0.9.0)
    pip install splinter -U

For other OS and browsers check package documentation directly:
* `Geckodriver <https://github.com/mozilla/geckodriver>`__
* `Selenium <https://github.com/SeleniumHQ/selenium>`__
* `Splinter <https://github.com/cobrateam/splinter>`__

Warning! There is inconsistency issues with browser tests and if you suspect your
changes did not break the tests we suggest you rerun the test before
starting debugging more.

Known issues:
* With Chrome test `E-Commerce_tests/browser/front/test_checkout_with_login_and_register.py`
is very unstable.

Collecting translatable messages
--------------------------------

To update the PO catalog files which contain translatable (and
translated) messages, issue ``E-Commerce_makemessages`` management command in
the ``E-Commerce`` directory:

.. code-block:: shell

   cd E-Commerce && python -m E-Commerce_workbench E-Commerce_makemessages
