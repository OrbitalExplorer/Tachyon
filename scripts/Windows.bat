@echo off
:loop
java -Xmx3G -Xms3G -jar quilt-server-launch.jar nogui
set /a t=10
:countdown
cls
echo Restart in %t% seconds, press C to cancel:
choice /c YC /n /t 1 /d Y > nul
if errorlevel 2 (
    echo You cancelled shutdown
    exit 0
)
set /a t-=1
if %t% gtr 0 goto countdown

echo Restarting ...

goto loop

pause