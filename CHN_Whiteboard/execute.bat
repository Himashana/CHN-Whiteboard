@echo off
echo -----------------------------------------------------------------------------------
echo execute.bat is executing commands... The app launcher will initialize shortly.
echo -----------------------------------------------------------------------------------
echo Creating tmp folder...
mkdir tmp

echo Copying files...
copy execute.py tmp
copy CSSrefresh.js tmp
copy PackageManager.py tmp
copy service.js tmp
copy stoped.html tmp
copy Update.js tmp
copy Whiteboard.html tmp
copy index.html tmp
copy pagecontroller.html tmp
copy canvas_setup.js tmp

cd tmp

echo Starting execute.py ...
execute.py

cd ..