@echo off 
:start 
java -Xmx3G -Xms3G -jar quilt-server-launch.jar nogui 
set /a "t=10" 
:loop 
set /a "t-=1" 
if "" == "0" goto timedout 
cls 
choice /T 1 /C sc /N /D s /M "Restart in  seconds, press C to cancel: " 
if not "0" == "1" goto cancelled  
goto :loop 
:cancelled 
echo You cancelled shutdown 
goto :end 
:timedout 
echo Restarting down 
goto :start 
:end 
pause 
