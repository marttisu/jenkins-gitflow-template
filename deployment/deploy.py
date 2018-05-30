#!/usr/bin/env python
"""Deploy the application."""

import argparse
import logging

logging.basicConfig(format='%(asctime)s '+logging.BASIC_FORMAT,
                    datefmt='%Y-%m-%dT%H:%M:%S%z',
                    level=logging.INFO)
LOGGER = logging.getLogger(__name__)


def get_argument_parser():
    """Get argument parser."""
    parser = argparse.ArgumentParser(
        description='Deploy application.')
    parser.add_argument('environment', type=str,
                        choices=['dev', 'tst', 'qa', 'prd'],
                        help='The name of the environment')
    return parser


def deploy(environment):
    """Deploy application."""
    return


def main():
    """Deploy application."""
    args = get_argument_parser().parse_args()
    LOGGER.info('Deploying to environment {}'.format(args.environment))
    deploy(environment=args.environment)
    LOGGER.info('Done')


if __name__ == '__main__':
    main()
