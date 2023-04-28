import logging as logger
import os
import sys
import six
from PyQt5.QtWidgets import QApplication
from trial_02 import CreateXlsDialog

# from pprint import pprint


print(os.path.dirname(sys.argv[0]))
logfile = os.path.dirname(sys.argv[0]) + "/log/test_han.log"


class ShotgunActionException(Exception):
    pass


class ShotgunAction:
    def __init__(self, url):
        self.logger = self._init_log(logfile)

        self.url = url
        self.protocol, self.action, self.params = self._parse_url()

        self.entity_type = self.params["entity_type"]
        logger.info("params: %s" % self.entity_type)

        # ids of entities that were currently selected
        self.selected_ids = []
        if len(self.params["selected_ids"]) > 1:
            sids = self.params["selected_ids"].split(",")
            self.selected_ids = [int(id) for id in sids]

        else:
            self.selected_ids = self.params["selected_ids"]
        logger.info("params: %s" % self.selected_ids)

        # check action
        if self.action == 'processVersion':
            self.processVersion()
            app = QApplication(sys.argv)
            du = CreateXlsDialog()
            du.show()
            print("456")
            du.okBtn.clicked.connect(self.okBtn_clicked)
            print("123")
            sys.exit(app.exec_())

        else:
            print("No Action")

    def processVersion(self):
        data = [self.entity_type, self.selected_ids]

        return data

    def okBtn_clicked(self):
        print("hi")

    def _init_log(self, filename="test_han.log"):
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
        logger.info("ami_handler logging started.")
        return logger

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



if __name__ == "__main__":
    sa = ShotgunAction(sys.argv[1])