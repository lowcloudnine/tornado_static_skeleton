# -*- coding: utf-8 -*-
"""
Purpose
-------

    A central file for handling all of the connection brokers tornado
    handlers.

--------

"""
# ----------------------------------------------------------------------------
# Imports
# ----------------------------------------------------------------------------


# ---- Standard Libraries

# ---- External Libraries
import tornado.web


# ----------------------------------------------------------------------------
# Authorship
# ----------------------------------------------------------------------------

__author__ = 'Jon Schiefelbein'
__email__ = 'lowcloudnine@hotmail.com'

# ----------------------------------------------------------------------------
# Classes:  *Handlers
# ----------------------------------------------------------------------------


class IndexHandler(tornado.web.RequestHandler):
    """ Handles the main part of the web site, i.e. the index. """
    def get(self, page_title="Tornado Static Template"):
        """ for GET request renders index.html """
        self.render("index.html",
                    page_title=page_title)
