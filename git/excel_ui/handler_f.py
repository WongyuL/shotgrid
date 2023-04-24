import sys
import pprint
import os
import six
import logging as logger
from trial_02 import CreateXlsDialog
from PyQt5 import QtWidgets

# def main(args):
#     # Make sure we have only one arg, the URL
#     if len(args) != 1:
#         sys.exit("This script requires exactly one argument")
#
#     # Make sure the argument have a : symbol
#     if args[0].find(":") < 0:
#         sys.exit("The argument is a url and requires the symbol ':'")
#
#     # Parse the URL
#     protocol, fullPath = args[0].split(":", 1)
#
#     # If there is a querystring, parse it
#     if fullPath.find("?") >= 0:
#         path, fullArgs = fullPath.split("?", 1)
#         action = path.strip("/")
#         params = parse_qs(fullArgs)
#     else:
#         action = fullPath.strip("/")
#         params = ""
#
#     # This is where you can do something productive based on the params and the
#     # action value in the URL. For now we'll just print out the contents of the
#     # parsed URL.
#     fh = open('output.txt', 'w')
#     fh.write(pprint.pformat((protocol, action, params)))
#     fh.close()
#
#     #show UI
#     app = QtWidgets.QApplication(sys.argv)
#     dialog = CreateXlsDialog()
#     dialog.show()


# SERVER_PATH = 'https://rndtest.shotgrid.autodesk.com'
# SCRIPT_NAME = 'script_wongyu'
# SCRIPT_KEY = 'stunj5lyzpkQyeapzrbdejd-b'
# ---------------------------------------------------------------------------------------------
# Variables
# ---------------------------------------------------------------------------------------------
# location to write logfile for this script
# logging is a bit of overkill for this class, but can still be useful.
print(os.path.dirname(sys.argv[0]))
logfile = os.path.dirname(sys.argv[0]) + "/test_han.log"


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
        self.logger = self._init_log(logfile)
        self.url = url
        self.protocol, self.action, self.params = self._parse_url()

        # entity type that the page was displaying
        self.entity_type = self.params["entity_type"]
        logger.info("params: %s" % self.entity_type)

        self.selected_ids = []
        if len(self.params["selected_ids"]) > 1:
            sids = self.params["selected_ids"].split(",")
            self.selected_ids = [int(id) for id in sids]

        else:
            self.selected_ids = self.params["selected_ids"]
        logger.info("params: %s" % self.selected_ids)

        if self.action == 'processVersion':
            app = QtWidgets.QApplication(sys.argv)
            dialog = CreateXlsDialog()
            dialog.show()
            dialog.sys.exit(app.exec_())
            sys.exit(app.exec_())

        else:
            print("No Action")

        # Project info (if the ActionMenuItem was launched from a page not belonging
        # to a Project (Global Page, My Page, etc.), this will be blank
        if "project_id" in self.params:
            self.project = {
                "id": int(self.params["project_id"]),
                "name": self.params["project_name"],
            }
        else:
            self.project = None

        # Internal column names currently displayed on the page
        self.columns = self.params["cols"]

        # Human readable names of the columns currently displayed on the page
        self.column_display_names = self.params["column_display_names"]

        # All ids of the entities returned by the query (not just those visible on the page)

        # All ids of the entities returned by the query in filter format ready
        # to use in a find() query
        # self.ids_filter = _convert_ids_to_filter(self.ids)

        # ids of entities that were currently selected
        # All selected ids of the entities returned by the query in filter format ready
        # to use in a find() query
        # self.selected_ids_filter = _convert_ids_to_filter(self.selected_ids)

        # sort values for the page
        # (we don't allow no sort anymore, but not sure if there's legacy here)
        if "sort_column" in self.params:
            self.sort = {
                "column": self.params["sort_column"],
                "direction": self.params["sort_direction"],
            }
        else:
            self.sort = None

        # title of the page
        self.title = self.params["title"]

        # user info who launched the ActionMenuItem
        self.user = {"id": self.params["user_id"], "login": self.params["user_login"]}

        # session_uuid
        self.session_uuid = self.params["session_uuid"]

        if self.action == 'processVersion':
            app = QtWidgets.QApplication(sys.argv)
            dialog = CreateXlsDialog()
            dialog.show()
            dialog.sys.exit(app.exec_())
            sys.exit(app.exec_())

    # ----------------------------------------------
    # Set up logging
    # ----------------------------------------------
    def _init_log(self, filename="handler_f.log"):
        try:
            logger.basicConfig(
                level=logger.DEBUG,
                format="%(asctime)s %(levelname)-8s %(message)s",
                datefmt="%Y-%b-%d %H:%M:%S",
                filename=filename,
                filemode="w+",
            )
        except IOError as e:
            raise ShotgunActionException("Unable to open logfile for writing: %s" % e)
        logger.info("ShotgunAction logging started.")
        return logger

        # ----------------------------------------------

    # Parse ActionMenuItem call into protocol, action and params
    # ----------------------------------------------
    def _parse_url(self):
        logger.info("Parsing full url received: %s" % self.url)

        # get the protocol used
        protocol, path = self.url.split(":", 1)
        logger.info("protocol: %s" % protocol)

        # extract the action
        action, params = path.split("?", 1)
        action = action.strip("/")
        logger.info("action: %s" % action)

        # extract the parameters
        # 'column_display_names' and 'cols' occurs once for each column displayed so we store it as a list
        params = params.split("&")
        p = {"column_display_names": [], "cols": []}
        for arg in params:
            key, value = map(six.moves.urllib.parse.unquote, arg.split("=", 1))
            if key == "column_display_names" or key == "cols":
                p[key].append(value)
            else:
                p[key] = value
        params = p
        logger.info("params: %s" % params)
        return protocol, action, params

    # ----------------------------------------------
    # Convert IDs to filter format to us in find() queries
    # ----------------------------------------------


# ----------------------------------------------
# Main Block
# ----------------------------------------------
if __name__ == "__main__":
    sa = ShotgunAction(sys.argv[1])


    # try:
    #     sa = ShotgunAction(sys.argv[1])
    #     logger.info("ShotgunAction: Firing... %s" % (sys.argv[1]))
    # except IndexError as e:
    #     raise ShotgunActionException("Missing GET arguments")
    # logger.info("ShotgunAction process finished.")
    # sys.exit(main(sys.argv[1:]))


