================
compare_versions
================

.. image:: https://img.shields.io/pypi/v/compare_versions.svg
    :target: https://pypi.python.org/pypi/compare_versions
    :alt: PyPI Version

.. image:: https://travis-ci.org/lukeyeager/compare-versions.svg?branch=master
    :target: https://travis-ci.org/lukeyeager/compare-versions
    :alt: Build Status

.. image:: https://landscape.io/github/lukeyeager/compare-versions/master/landscape.svg?style=flat
    :target: https://landscape.io/github/lukeyeager/compare-versions/master
    :alt: Code Health

.. image:: https://coveralls.io/repos/lukeyeager/compare-versions/badge.svg?branch=master&service=github
    :target: https://coveralls.io/github/lukeyeager/compare-versions?branch=master
    :alt: Code Coverage

Compare versions using various versioning schemes.

*Example usage:* ::

    $ compare_versions 1.0.0 1.0.0-dev --scheme semver
    1.0.0 > 1.0.0-dev

    $ compare_versions 1.0.0 1.0.0-dev --scheme string
    1.0.0 < 1.0.0-dev
