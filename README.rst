================
compare_versions
================

Compare versions using various versioning schemes.

*Example usage:* ::

    $ compare_versions 1.0.0 1.0.0-dev --scheme semver
    1.0.0 > 1.0.0-dev

    $ compare_versions 1.0.0 1.0.0-dev --scheme string
    1.0.0 < 1.0.0-dev
