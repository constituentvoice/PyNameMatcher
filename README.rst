PyNameMatcher
=============
Help with matching names to nick-names and vice-versa. Based on data by https://github.com/carltonnorthern/nickname-and-diminutive-names-lookup

INSTALL
-------

.. code-block::

    $ pip install PyNameMatcher


USAGE
-----
.. code-block::

    from pynamematcher import PyNameMatcher

    matcher = PyNameMatcher(data_file=path_to_datafile)
    possible_names = matcher.match('Bob')



DOCUMENTATION
-------------

`__init__()` Options

:data_file:     Path to a CSV formatted data file of names. Defaults to an internal data file.

:use_metaphone: Match names using the metaphone library to catch misspellings.

`match()` Options

:name:  First argument. The name to match

:use_metaphone: used internally when `self.use_metaphone` is `True`

:remove_match:  Remove the input name (default `True`). Used internally to keep
                names when searching metaphone symbols.

:empty_match_returns_none:  If no names match the method will return None instead of the empty set
                            this is to enable the behavior of versions before 0.2. (default `False`)

AUTHOR
------
Chris Brown - chris.brown@constituentvoice.com

LICENSE
-------
Licensed under Apache License 2.0. Copyright 2019-2022 Constituent Voice LLC.

See LICENSE for complete terms.



