#!/usr/bin/env bash
# -*- coding: utf-8 -*-
#
# This file is part of Dictdiffer.
#
# Copyright (C) 2013 Fatih Erikli.
# Copyright (C) 2014, 2016 CERN.
# Copyright (C) 2019 ETH Zurich, Swiss Data Science Center, Jiri Kuncar.
#
# Dictdiffer is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more
# details.

pydocstyle dictdiffer && \
pytest --cov=dictdiffer --cov-report=term-missing --capture=sys -vv tests
