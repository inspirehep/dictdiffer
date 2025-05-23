# This file is part of Dictdiffer.
#
# Copyright (C) 2015, 2016 CERN.
#
# Dictdiffer is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more
# details.

"""Python compatibility definitions."""

__all__ = ("Iterable", "MutableMapping", "MutableSequence", "MutableSet")

try:
    PY2 = True
    string_types = (basestring,)
    text_type = unicode
    num_types = int, long, float
except NameError:
    PY2 = False
    string_types = (str,)
    text_type = str
    num_types = int, float

if PY2:
    from collections import Iterable, MutableMapping, MutableSequence, MutableSet
    from itertools import izip_longest as _zip_longest
else:
    from collections.abc import Iterable, MutableMapping, MutableSequence, MutableSet
    from itertools import zip_longest as _zip_longest

izip_longest = _zip_longest
