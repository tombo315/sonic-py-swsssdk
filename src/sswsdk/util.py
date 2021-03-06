"""
Syslog and daemon script utility library.
"""

import json
import logging
import logging.config
import sys
from getopt import getopt


# TODO: move to dbsync project.
def usage(script_name):
    print('Usage: python ', script_name,
          '-d [logging_level] -f [update_frequency] -h [help]')


# TODO: move to dbsync project.
def process_options(script_name):
    """
    Process command line options
    """
    options, remainders = getopt(sys.argv[1:], "d:f:h", ["debug=", "frequency=", "help"])

    args = {}
    for (opt, arg) in options:
        if opt in ('-d', '--debug'):
            args['log_level'] = int(arg)
        elif opt in ('-f', '--frequency'):
            args['update_frequency'] = int(arg)
        elif opt in ('-h', '--help'):
            usage(script_name)

    return args


# TODO: move
def setup_logging(config_file_path, log_level=logging.INFO):
    """
    Logging configuration helper.

    :param config_file_path: file path to logging configuration file.
    https://docs.python.org/3/library/logging.config.html#object-connections
    :param log_level: defaults to logging.INFO
    :return: None - access the logger by name as described in the config--or the "root" logger as a backup.
    """
    try:
        with open(config_file_path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    except (ValueError, IOError, OSError):
        # json.JSONDecodeError is throwable in Python3.5+ -- subclass of ValueError
        logging.basicConfig(log_level=log_level)
        logging.root.exception(
            "Could not load specified logging configuration '{}'. Verify the filepath exists and is compliant with: "
            "[https://docs.python.org/3/library/logging.config.html#object-connections]".format(config_file_path))
