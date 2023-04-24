# // cmdLine points to the foo path.
# //Add foo to the Os protocols and set foobar to handle the protocol
# QSettings fooKey("HKEY_CLASSES_ROOT\\foo", QSettings::NativeFormat);
# mxKey.setValue(".", "URL:foo Protocol");
# mxKey.setValue("URL Protocol", "");
# QSettings fooOpenKey("HKEY_CLASSES_ROOT\\foo\\shell\\open\\command", QSettings::NativeFormat);
# mxOpenKey.setValue(".", cmdLine);

from PyQt5.QtCore import QSettings

key = QSettings("HKEY_CLASSES_ROOT\\ShotGrid", QSettings.NativeFormat)
key.setValue("", "URL:ShotGrid Protocol")
key.setValue("URL Protocol", "")
key.beginGroup("shell")
key.beginGroup("open")
key.beginGroup("command")
key.setValue("", 'python3 "C:\\Users\\admin\\excel_ui\\shotgun_ami_handler.py" "%1"')
key.endGroup()
key.endGroup()
key.endGroup()

