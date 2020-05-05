#!/usr/bin/env python
from os import environ
from sys import argv


def main():
    environ.setdefault('DJANGO_SETTINGS_MODULE', 'web.settings')
    try:
        from django.core.management import execute_from_command_line
        from django.core.management.commands.runserver import Command
        Command.default_port = "25565"
    except ImportError:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from ImportError
    execute_from_command_line(argv)


if __name__ == '__main__':
    main()
