# Copyright (C) 2023 Red Hat
# SPDX-License-Identifier: Apache-2.0


import os
import logging

import requests


class SimpleFluentBitHTTPInputHandler(logging.Handler):
    """A minimal handler for sending logs to the HTTP Input
    of a Fluent Bit collector."""
    def __init__(self, url):
        logging.Handler.__init__(self)
        self.url = url


    def emit(self, record):
        d = {
            'log': self.format(record)
        }
        for envvar in os.environ:
            if envvar.startswith('K8S_'):
                key = envvar[4:].lower().replace('_', '.')
                d[key] = os.environ[envvar]
        try:
            req = requests.post(self.url, json=d)
            req.raise_for_status()
        except requests.HTTPError as e:
            self.handleError(record)