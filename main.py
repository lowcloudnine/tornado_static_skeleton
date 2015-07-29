#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Purpose
-------

Starts a minimal Tornado server on the port specified and serving index.html
from templates.

>>> main.py --port=8000
Tornado started and listening on port 8080

will start the server on port 8000.

"""
# ----------------------------------------------------------------------------
# Imports
# ----------------------------------------------------------------------------


# ---- Standard Libraries
import os.path

# ---- External Libraries
import tornado.httpserver
import tornado.ioloop
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
    """ Creates an instance of a tornado web application. """

    def __init__(self):
        """ Uses the inherited options to create handlers and settings. """
        settings = {
            "template_path": os.path.join(
                os.path.dirname(__file__), "templates"),
            "static_path": os.path.join(os.path.dirname(__file__), "static"),
            "autoreload":  True,
            "compress_response":  True,
        }

        the_handlers = [
            (r"/", IndexHandler),
        ]

        tornado.web.Application.__init__(self, the_handlers, **settings)

# ----------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------


def main():
    """ Runs the script as a stand alone application. """
    # ---- Options and Command Line Parsing
    tornado.options.define("port",
                           default=8080,
                           help="run on the given port",
                           type=int)
    tornado.options.parse_command_line()

    # ---- Create the application with the needed handlers and settings
    app = Application()

    # ---- Running the Server
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(tornado.options.options.port)
    print("Tornado started and listening on port {}"\
          .format(tornado.options.options.port))
    tornado.ioloop.IOLoop.instance().start()

# ----------------------------------------------------------------------------
# Name
# ----------------------------------------------------------------------------


if __name__ == "__main__":
    main()
