Contributing
============

As an open source platform under active development, E-Commerce gladly
welcomes all contributions and feedback. As soon as you
learn `E-Commerce basics <http://E-Commerce.readthedocs.io/en/latest/>`_,
you can contribute in several ways:

* Join our `community forums <https://community.E-Commerce.com/forums/>`_
  and `gitter group <https://gitter.im/E-Commerce/E-Commerce>`_ to help answer questions.
* Report issues on our `issue tracker <https://E-Commerceteam.atlassian.net/issues>`_.
* Submit pull requests for new or corrected behavior.
* Improve the `developer documentation <http://E-Commerce.readthedocs.io/en/latest/>`_.
* Improve the `merchant documentation <http://E-Commerce-guide.readthedocs.io/en/latest/>`_.
* Write unit tests.

Reporting an issue
------------------

Before submitting an issue, please ensure you're using the latest version
of E-Commerce and search the forums and issue tracker to see if the issue has
already been reported.

If you're certain you've found an issue, we encourage you to report it
by clicking the "Provide feedback" trigger button to the right of the
screen. Please provide detailed steps to recreate the bug.
The more details provided, the better!

.. _submit-a-pull-request:

Submit a Pull Request
---------------------

We love receiving pull requests from the community and will do our
best to process them quickly. Before you start development,
ensure a related issue doesn't exist. If you plan on making a
significant code/design change, please document it in our issue tracker.
If you'd like to work on an issue on our backlog, please ping us on gitter.

Process
^^^^^^^

* Fork our `Github repository <https://github.com/E-Commerce/E-Commerce>`_ and create your branch from master.
* Create your patch and add appropriate test cases.
* Add a changelog entry
* Write down the issue number (if working on a ticket) in the commit and PR description

Once your PR is submitted, our CI environment will ensure the code follows our
guidelines and tests pass. Members of our core team will then review the changes
and provide feedback, if required.

Coding Style
------------

As a project built on Django, E-Commerce adheres to the
`Django code styles <https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/>`_

Improving the Documentation
---------------------------

Not sure if that typo is worth a pull request? Do it! We encourage any
general improvements or new additions to our documentation.

Our documentation is written in reStructuredText using the Sphinx documentation generator.

Writing Unit Tests
------------------

Want to learn more about E-Commerce internals? Adding unit tests that increase
our test coverage is a great way for new contributors to get started with
E-Commerce development.

Process
^^^^^^^

* Fork the repo and create your branch from master.
* run our current test suite with coverage

  .. code-block:: shell

     py.test -vvv --nomigrations --cov E-Commerce --cov-report html E-Commerce_tests

* View the built report to find areas currently lacking tests
* Add your test to ``E-Commerce_tests/``.
* :ref:`submit-a-pull-request`
