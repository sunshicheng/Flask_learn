#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging.config, logging , yaml


logging.config.dictConfig(yaml.load(open('./logging.conf'),Loader=yaml.FullLoader))

FileLogger = logging.getLogger('file')