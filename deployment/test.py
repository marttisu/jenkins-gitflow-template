#!/usr/bin/env python
"""Test the application."""

import logging

logging.basicConfig(format='%(asctime)s '+logging.BASIC_FORMAT,
                    datefmt='%Y-%m-%dT%H:%M:%S%z',
                    level=logging.INFO)
LOGGER = logging.getLogger(__name__)


def test():
    """Test application."""
    return


def main():
    """Test application."""
    LOGGER.info('Testing the application')
    test()
    LOGGER.info('Done')


if __name__ == '__main__':
    main()
