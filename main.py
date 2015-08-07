#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Purpose
-------

Starts a minimal Tornado server on the port specified and serving index.html
from templates.

>>> import main
>>> main.main()
Tornado started and listening on port 8000

will start the server on port 8000.

"""
# ----------------------------------------------------------------------------
# Imports
# ----------------------------------------------------------------------------


# ---- Standard Libraries
import datetime
import logging
import os.path
import sys

# ---- External Libraries
import tornado.httpserver
import tornado.ioloop
import tornado.log
import tornado.options
import tornado.web

# ---- Custom Libraries
from handlers.index_handler import IndexHandler

# ----------------------------------------------------------------------------
# Authorship
# ----------------------------------------------------------------------------


__author__ = 'Jon Schiefelbein'
__email__ = 'lowcloudnine@hotmail.com'

# ----------------------------------------------------------------------------
# Class:  Application
# ----------------------------------------------------------------------------


class Application(tornado.web.Application):
    """ Creates an instance of a tornado web application.
    Uses the __init__ from parent to initialize a tornado web application.

    """
    def __init__(self):
        """ Uses the inherited options to create handlers and settings. """
        settings = {
            "template_path": os.path.join(
                os.path.dirname(__file__), "templates"),
            "static_path": os.path.join(os.path.dirname(__file__), "static"),
            "compress_response":  True,
        }

        the_handlers = [
            (r"/", IndexHandler),
        ]

        # could use super().__init__(self, the_handlers, **settings) to
        # give the code a more OO feel but that only works in Python 3
        # the line below has been tested in both Python 2.7 and 3.4
        tornado.web.Application.__init__(self, the_handlers, **settings)

# ----------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------


def main():
    """ Runs the script as a stand alone application. """
    # ---- use current date and time to generate log file name
    now = datetime.datetime.now()
    datetime_stamp = datetime.datetime.strftime(now, "%Y-%d-%m-%H%M%S")
    log_dir = "logs/"

    # ---- Tornado definitions
    tornado.options.define("port",
                           default=8080,
                           help="run on the given port",
                           type=int)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Set up log files

    # ---- Set up Access Log
    access_log = tornado.log.access_log
    access_log_file = log_dir + "access/tornado_access_" + \
                      datetime_stamp + ".log"
    access_log_handler = logging.handlers.\
        RotatingFileHandler(access_log_file,
                            maxBytes=1024*100,
                            backupCount=10)
    access_log.addHandler(access_log_handler)

    # ---- Set up Application Log
    app_log = tornado.log.app_log
    app_log_file = log_dir + "application/tornado_app_" + \
                   datetime_stamp + ".log"
    app_log_handler = logging.handlers.\
        RotatingFileHandler(app_log_file,
                            maxBytes=1024*100,
                            backupCount=4)
    app_log.addHandler(app_log_handler)

    # ---- Set up General/Main Log
    gen_log = tornado.log.gen_log
    gen_log_file = log_dir + "tornado_" + \
                   datetime_stamp + ".log"
    gen_log_handler = logging.handlers.\
        RotatingFileHandler(gen_log_file,
                            maxBytes=1024*100,
                            backupCount=4)
    gen_log.addHandler(gen_log_handler)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # ---- Parse any options from the command line and configuration file
    tornado.options.parse_command_line()
    tornado.options.parse_config_file("config.py")

    # ---- Running the Server
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(tornado.options.options.port)
    print("Tornado started and listening on port {}"
          .format(tornado.options.options.port))
    tornado.ioloop.IOLoop.instance().start()

# ----------------------------------------------------------------------------
# Name
# ----------------------------------------------------------------------------


if __name__ == "__main__":
    main()
