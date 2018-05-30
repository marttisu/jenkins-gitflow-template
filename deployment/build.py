#!/usr/bin/env python
"""Build the application."""

import logging

logging.basicConfig(format='%(asctime)s '+logging.BASIC_FORMAT,
                    datefmt='%Y-%m-%dT%H:%M:%S%z',
                    level=logging.INFO)
LOGGER = logging.getLogger(__name__)


def build():
    """Build application."""
    return


def main():
    """Build application."""
    LOGGER.info('Building the application')
    build()
    LOGGER.info('Done')


if __name__ == '__main__':
    main()
