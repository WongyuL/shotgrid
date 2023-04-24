import sys
from PySide2 import QtWidgets
from test_excel import CreateXlsDialog
import sgtk
from shotgun_api3 import Shotgun

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    site_url = 'https://rndtest.shotgrid.autodesk.com/page/7434'
    script_name = 'script_wongyu'
    script_key = 'mWum6vnnrxfn%wtaoutismjiw'
    auth_args = {'login': script_name, 'password': script_key}
    
    sg = Shotgun(site_url, **auth_args)

    url = sys.argv[1]
    url_parts = urlparse(url)
    entity_type = url.parts.path.split('/')[1]
    entity_
    # Parse the URL to extract any parameters or data you need
    # ...

    dlg = CreateXlsDialog()
    if dlg.exec_():
        path = dlg.getPath()
        # Write your logic to create the Excel file at the given path here
        # ...

    sys.exit(app.exec_())