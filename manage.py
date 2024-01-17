#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    # Set the default Django settings module for the command-line utility
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movies_api.settings')
    
    try:
        # Import the execute_from_command_line function from django.core.management
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Handle ImportError if Django is not installed or not available
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Execute the management commands from the command line
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    # Execute the main function if this script is being run directly
    main()
