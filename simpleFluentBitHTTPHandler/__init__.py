# Copyright (C) 2023 Red Hat
# SPDX-License-Identifier: Apache-2.0


import logging

import requests


class SimpleFluentBitHTTPHandler(logging.Handler):
    def __init__(self, url):
        logging.Handler.__init__(self)
        self.url = url

    def emit(self, record):
        d = {
            'log': self.format(record)
        }
        try:
            req = requests.get(self.url, json=d)
            req.raise_for_status()
        except requests.HTTPError as e:
            self.handleError(record)