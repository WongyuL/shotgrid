import shotgun_api3
import os
import json
import urllib.parse
import sys

arg = sys.argv[1]
handler, fullPath = arg.split(":", 1)
path, fullArgs = fullPath.split("?", 1)
action = path.strip("/")
args = fullArgs.split("&")
get_dict = {}
for arg in args:
    key, value = map(urllib.parse.unquote, arg.split('=', 1))
    get_dict[key] = value

if action == "ami_test":

    file = open("\C:\\Users\\admin\\excel_ui\\hello_test.txt", "w")

    sg = shotgun_api3.Shotgun(
        "https://rndtest.shotgrid.autodesk.com",
        login=os.environ["script_wongyu"],
        password=os.environ["mWum6vnnrxfn%wtaoutismjiw"],
    )
    project = sg.find_one("Project", [])

    file.write(json.dumps(project, indent=4))

    file.close()

if action == "ami_test_2":
    file = open("\C:\\Users\\admin\\excel_ui\\hello_test.txt", "w")

    file.write("No action here!")

    file.close()