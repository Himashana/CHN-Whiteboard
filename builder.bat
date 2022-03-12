@echo off
del Build
mkdir Build
copy CHN_Whiteboard\execute.bat Build
copy CHN_Whiteboard\execute.py Build
copy CHN_Whiteboard\CSSrefresh.js Build
copy CHN_Whiteboard\index.html Build
copy CHN_Whiteboard\PackageManager.py Build
copy CHN_Whiteboard\pagecontroller.html Build
copy CHN_Whiteboard\service.js Build
copy CHN_Whiteboard\stoped.html Build
copy CHN_Whiteboard\Update.js Build
copy CHN_Whiteboard\Whiteboard.html Build
copy CHN_Whiteboard\imgtodataURL.py Build
cd Build
mkdir out
ECHO Building exe...
pyinstaller.exe --onefile imgtodataURL.py
ECHO Build compleated.
del builder.bat
cd ..