# Copyright (C) 2023 Red Hat
# SPDX-License-Identifier: Apache-2.0


from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Simple Fluent Bit HTTP Log Handler'
LONG_DESCRIPTION = '''
The handler sends a log line as a JSON payload to a Fluent Bit HTTP input.
'''

setup(
        name="simpleFluentBitHTTPHandler", 
        version=VERSION,
        author="Matthieu Huin",
        author_email="mhuin@redhat.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['requests'],
        keywords=['python', 'fluent bit', 'logging'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "Programming Language :: Python :: 3",
            "Operating System :: OS Independent",
        ]
)