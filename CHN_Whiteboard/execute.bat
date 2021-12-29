@echo off

mkdir tmp
copy execute.py tmp
copy CSSrefresh.js tmp
copy PackageManager.py tmp
copy run.js tmp
copy service.js tmp
copy stoped.html tmp
copy Update.js tmp
copy Whiteboard.html tmp
copy index.html tmp
copy UpdateJScode.py tmp

cd tmp

execute.py

cd ..