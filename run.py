# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os

from sys import exit


from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run()
