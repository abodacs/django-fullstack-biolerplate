#!/usr/bin/env python

import os
import sys
from pathlib import PurePath

from decouple import AutoConfig

BASE_DIR = PurePath(__file__).parent
config = AutoConfig(search_path=BASE_DIR)

if __name__ == "__main__":
    settings_module = config("DJANGO_SETTINGS_MODULE", default=None)
    if sys.argv[1] == "test":
        if settings_module:
            print(
                "Ignoring config('DJANGO_SETTINGS_MODULE') because it's test. "
                "Using 'djangoFullstack.settings.test'"
            )
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoFullstack.settings.test")
    else:
        if settings_module is None:
            print("Error: no DJANGO_SETTINGS_MODULE found. Will NOT start devserver. "
                  "Remember to create .env file at project root. "
                  "Check README for more info.")
            sys.exit(1)
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
