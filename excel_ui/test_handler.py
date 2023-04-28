import urllib.parse

import shotgun_api3
import json
import sys
from test_excel import CreateXlsDialog


print(sys.argv[1])
arg = sys.argv[1]

handler, fullPath = arg.split(":", 1)
path, fullArgs = fullPath.split("?", 1)
action = path.strip("/")
args = fullArgs.split("&")
get_dict = {}
for arg in args:
    key, value = map(urllib.parse.unquote, arg.split('=', 1))
    get_dict[key] = value

if action == "test_action":
    file = open("C:\\Users\\admin\\excel_ui\\test_handler.txt", "w")

    sg = shotgun_api3.Shotgun(
        "https://rndtest.shotgrid.autodesk.com",
        script_name="script_wongyu",
        api_key="nccysmaxvksdO7wggcinr%qxv"
    )

    asset = sg.find_one(
        get_dict["entity_type"],
        [
            ["id", "is", int(get_dict["selected_ids"])]
        ],
        ["shots", "code"],
    )
    # message = "%s is used in the following shots: %s" % (
    #     asset["code"], [x["name"] for x in asset["shots"]]
    # )

    # project = sg.find_one("Project", [])

    file.write("hell")

    file.close()
