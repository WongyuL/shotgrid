#!/usr/bin/env python
# encoding: utf-8

# ---------------------------------------------------------------------------------------------
# Description
# ---------------------------------------------------------------------------------------------
"""
The values sent by the Action Menu Item are in the form of a GET request that is similar to the
format: myCoolProtocol://doSomethingCool?user_id=24&user_login=shotgun&title=All%20Versions&...

In a more human-readable state that would translate to something like this:
{
    'project_name': 'Demo Project',
     'user_id': '24',
     'title': 'All Versions',
     'user_login': 'shotgun',
     'sort_column': 'created_at',
     'entity_type': 'Version',
     'cols': 'created_at',
     'ids': '5,2',
     'selected_ids': '2,5',
     'sort_direction': 'desc',
     'project_id': '4',
     'session_uuid': 'd8592bd6-fc41-11e1-b2c5-000c297a5f50',
     'column_display_names':
    [
        'Version Name',
         'Thumbnail',
         'Link',
         'Artist',
         'Description',
         'Status',
         'Path to frames',
         'QT',
         'Date Created'
    ]
}

This simple class parses the url into easy to access types variables from the parameters,
action, and protocol sections of the url. This example url
myCoolProtocol://doSomethingCool?user_id=123&user_login=miled&title=All%20Versions&...
would be parsed like this:

    (string) protocol: myCoolProtocol
    (string) action: doSomethingCool
    (dict)   params: user_id=123&user_login=miled&title=All%20Versions&...

The parameters variable will be returned as a dictionary of string key/value pairs. Here's
how to instantiate:

  sa = ShotgunAction(sys.argv[1]) # sys.argv[1]

  sa.params['user_login'] # returns 'miled'
  sa.params['user_id'] # returns 123
  sa.protocol # returns 'myCoolProtocol'
"""

# ---------------------------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------------------------
import sys
import os
import sgtk
import six
import subprocess
import urllib.parse
from pywin.Demos.sliderdemo import MyDialog
from shotgun_api3 import Shotgun

# from test_excel import CreateXlsDialog

# ---------------------------------------------------------------------------------------------
# # Variables
# # ---------------------------------------------------------------------------------------------
shotgun_conf = {
    'url': 'https://rndtest.shotgrid.autodesk.com',
    'name': 'script_wongyu',
    'key': 'stunj5lyzpkQyeapzrbdejd-b'
}

# logfile = os.path.dirname(sys.argv[0]) + "/shotgun_action.log"

import sys
import pprint
try:
    from urlparse import parse_qs
except ImportError:
    from urllib.parse import parse_qs

def main(args):
    # Make sure we have only one arg, the URL
    if len(args) != 1:
        sys.exit("This script requires exactly one argument")

    # Make sure the argument have a : symbol
    if args[0].find(":") < 0:
        sys.exit("The argument is a url and requires the symbol ':'")

    # Parse the URL
    protocol, fullPath = args[0].split(":", 1)

    # If there is a querystring, parse it
    if fullPath.find("?") >= 0:
        path, fullArgs = fullPath.split("?", 1)
        action = path.strip("/")
        params = parse_qs(fullArgs)
    else:
        action = fullPath.strip("/")
        params = ""

    # This is where you can do something productive based on the params and the
    # action value in the URL. For now we'll just print out the contents of the
    # parsed URL.
    fh = open('output.txt', 'w')
    fh.write(pprint.pformat((protocol, action, params)))
    fh.close()
# ----------------------------------------------
# Generic ShotgunAction Exception Class
# ----------------------------------------------
class ShotgunActionException(Exception):
    pass


# ----------------------------------------------
# ShotgunAction Class to manage ActionMenuItem call
# ----------------------------------------------
class ShotgunAction:
    def __init__(self, url):
        # self.logger = self._init_log(logfile)
        self.entity_type = None
        self.url = url
        self.protocol, self.action, self.params = self._parse_url()
        self.selected_ids = []
        if len(self.params["selected_ids"]) > 0:
            sids = self.params["selected_ids"].split(",")
            self.selected_ids = [int(id) for id in sids]

    # ----------------------------------------------
    # Launch UI
    # ----------------------------------------------

    # def launch_ui(self, entity_type, entity_ids):
    #     url = f"ShotGrid://package_ver?entity_type={entity_type}&entity_ids={','.join(str(i) for i in entity_ids)}"

    # ui_script = "C:\\Users\\admin\\excel_ui\\test_excel.py"
    # cmd = [sys.executable, ui_script, url]
    # subprocess.Popen(cmd)

    def _parse_url(self):
        protocol, path = self.url.split(":", 1)
        action, params = path.split("?", 1)
        action = action.strip("/")
        params = params.split("&")
        p = {"column_display_names": [], "cols": []}
        for arg in params:
            key, value = map(six.moves.urllib.parse.unquote, arg.split("=", 1))
            if key == "column_display_names" or key == "cols":
                p[key].append(value)
            else:
                p[key] = value
        params = p
        # logger.info("params: %s" % params)
        return protocol, action, params

    # def launch_ui(entity_type, entity_ids):
    #     pass


    if __name__ == '__main__':
        sys.exit(main(sys.argv[1:]))

        # try:
    #     sa = ShotgunAction(sys.argv[1])
    #     sa.launch_ui(entity_type="SomeEntityType", entity_ids=[1, 2, 3])
    # # except IndexError, e:
    # #     raise ShotgunException("Missing POST arguments")
    # #     entity_type = sa.entity_type
    # #     entity_ids = sa.selected_ids
    # #     launch_ui(entity_type, entity_ids)
    # sg = Shotgun(shotgun_conf['url'], shotgun_conf['name'], shotgun_conf['key'], convert_datetimes_to_utc=convert_tz)
    # if sa.action == 'action_handler':
    #     result = packageFilesForClient
