@echo off
py -m pip install -r requirements.txt pyinstaller
py -m PyInstaller --noconfirm --windowed --name SwimGame --add-data "swim-game.html;." main.py
echo.
echo Done: dist\SwimGame\SwimGame.exe
pause
