@echo off
echo COM2TCP wird gestartet.
echo Dieses Fenster muss offen bleiben.
echo.
echo Bitte COM-Port eingeben (z.B. COM3):
set /p Port=

echo Es wurde %Port% gewaehlt.
@echo on 
com2tcp.exe --telnet --ignore-dsr --baud 115200 \\.\%Port% 23

echo Zum Beenden beliebige Taste druecken.
pause