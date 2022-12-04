"""
Script to initalize blink for an interactive session.

Load with:
>>> exec(open("./blinkapp/initialize_blink.py").read()); blink = start()
"""

import logging
from os import environ
from blinkpy.blinkpy import Blink
from blinkpy.auth import Auth
from blinkpy.helpers.util import json_load

logging.basicConfig(
    format="%(asctime)s,%(msecs)03d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
    datefmt="%Y-%m-%d:%H:%M:%S",
    level=logging.DEBUG,
)


HOME = environ.get("HOME")
CREDFILE = environ.get("CREDFILE", default=HOME + "/.blinkapp/creds")


def start():
    """Startup blink app."""
    blink = Blink()
    blink.auth = Auth(json_load(CREDFILE))
    blink.start()
    blink.save(CREDFILE)
    return blink

