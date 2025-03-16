#!/usr/bin/env python

# This file enables editable installs (pip install -e .[dev])

import setuptools

# ##########################################################
#  See this issue: https://github.com/pypa/pip/issues/7953
import site
import sys

site.ENABLE_USER_SITE = "--user" in sys.argv[1:]
# ##########################################################

if __name__ == "__main__":
    setuptools.setup( 
        name="flashcards-cli",
        version="0.1",
        packages=setuptools.find_packages(),
        install_requires=[
            "click",          # CLI үүсгэхэд шаардлагатай
            "flashcards-core" # flashcards-core сангаас хамаарна
        ],
        entry_points={
            "console_scripts": [
                "flashcards=flashcards_cli.main:main",  # CLI комманд
            ],
        },
        python_requires=">=3.8",  # Python 3.8 ба түүнээс дээш шаардлагатай
)
