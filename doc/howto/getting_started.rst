Installing E-Commerce
================

.. note::

   If you are planning on developing E-Commerce,
   read the :doc:`Getting Started with E-Commerce Development guide
   <getting_started_dev>` instead.

Requirements
------------

* Python 2.7.9+/3.4+. https://www.python.org/download/.
* Any database supported by Django.

Installation
------------

This guide assumes familiarity with the PyPA tools for Python packaging,
including ``pip`` and ``virtualenv``.

1. Update pip and setuptools

   .. code-block:: shell

      pip install -U pip
      pip install -U setuptools

2. Set up a new virtualenv for E-Commerce and activate it

   .. code-block:: shell

      virtualenv E-Commerce-venv
      . E-Commerce-venv/bin/activate

3. Install E-Commerce via pypi

   .. code-block:: shell

      pip install E-Commerce


4. Once installed, you can begin setting up a Django project using whichever
   standards you fancy. Refer to the top-level `settings
   <https://github.com/E-Commerce/E-Commerce/blob/master/E-Commerce_workbench/settings/base_settings.py>`_
   and `urls
   <https://github.com/E-Commerce/E-Commerce/blob/master/E-Commerce_workbench/urls.py>`_
   for configuration details. At minimum, you will need to add ``E-Commerce.core``
   to your ``INSTALLED_APPS``.

.. note::
   E-Commerce uses ``django-parler`` for model translations. Please ensure
   ``PARLER_DEFAULT_LANGUAGE_CODE`` is set. See `django-parler configuration
   <http://django-parler.readthedocs.io/en/latest/configuration.html>`_ for more
   details.

.. note::
   E-Commerce uses the ``LANGUAGES`` setting to render multilingual forms. You'll likely
   want to override this setting to restrict your applications supported languages.

5. Once you have configured the E-Commerce apps you would like to use, run the
   following commands to create the database and initialize E-Commerce

   .. code-block:: shell

      python manage.py migrate
      python manage.py E-Commerce_init


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


E-Commerce Packages
--------------

E-Commerce is a constellation of Django apps, with many delivered in the single
"E-Commerce Base" distribution, and with additional apps available as separate
downloads.

``E-Commerce.core`` is the core package required by all E-Commerce installations.
It contains the core business logic for e-commerce, and all of the database
models required. However, it contains no frontend or admin dashboard, as
different projects may wish to replace them with other components or even
elide them altogether.

``E-Commerce.front`` is a basic but fully featured storefront. It itself has
several sub-applications that may be used to toggle functionality on and off.

* ``E-Commerce.front.apps.auth`` is a wrapper around django auth for login and
  password recovery.
* ``E-Commerce.front.apps.registration`` provides views for customer activation
  and registration.
* ``E-Commerce.front.apps.customer_information`` provides views for customer
  address management.
* ``E-Commerce.front.apps.personal_order_history`` adds views for customer
  order history.
*  ``E-Commerce.front.apps.simple_order_notification`` can be used to send
   email notifications to the customer upon order completion.
* ``E-Commerce.front.apps.simple_search`` provides basic product search
  functionality.
* ``E-Commerce.front.apps.recently_viewed_products`` can be used to display the last
  five products viewed by the customer.

``E-Commerce.admin`` provides a fully featured administration dashboard.

``E-Commerce.addons`` can be used to install and manage E-Commerce addons.

``E-Commerce.api`` exposes E-Commerce APIs as RESTful url endpoints. See the
:doc:`web API documentation <../web_api>` for details.

``E-Commerce.campaigns`` provides a highly customizable promotion and discount
management system.

``E-Commerce.customer_group_pricing`` can be used to customize product pricing by
customer contact groups.

``E-Commerce.default_tax`` is a rules-based tax module that calculates and applies
taxes on orders. See the :doc:`prices and taxes documentation
<../ref/prices_and_taxes>` for details.

``E-Commerce.guide`` integrates search results from this documentation into Admin
search.

``E-Commerce.notify`` is a generic notification framework that can be used to
inform users about various events (order creation, shipments, password
resets, etc). See the :doc:`notification documentation
<../ref/notify_specification>` for details.

``E-Commerce.order_printouts`` adds support to create PDF printouts of orders from
admin.

``E-Commerce.simple_cms`` is a basic content management system that can be used to
add pages to the storefront.

``E-Commerce.simple_supplier`` is a simple inventory management system that can be
used to keep track of product inventory.
