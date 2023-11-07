# Copyright (C) 2023 Red Hat
# SPDX-License-Identifier: Apache-2.0


from logging.handlers import HTTPHandler

import requests


class SimpleFluentBitHTTPHandler(HTTPHandler):
    def __init__(self, url):
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