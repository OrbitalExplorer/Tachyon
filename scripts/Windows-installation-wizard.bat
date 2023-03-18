@echo off

set MINECRAFT_VERSION=1.19.2
set LOADER_VERSION=0.18.5
set FOLDER_PATH=%~dp0

if not exist usercache.json (
	color 3
	echo Getting Ready to install
	goto question

) else (
	color 4
	echo ERROR: It seems like the server is already installed.
	goto tut_question
)

:question
color 1
set /p input="Do You want to start the installation of the server? [y/n]: " 
if %input%==y (
	color 3
	echo Downloading QUILT Installer
	color 7
	bitsadmin.exe /transfer "QUILT Installer" https://maven.quiltmc.org/repository/release/org/quiltmc/quilt-installer/latest/quilt-installer-latest.jar %cd%\quilt-installer-latest.jar
	color 3
    echo Attempting to install the QUILT base server
	echo Installing to %CD%
	color 7
	java -jar quilt-installer-latest.jar install server %MINECRAFT_VERSION% %LOADER_VERSION% --install-dir=%FOLDER_PATH% --download-server
	goto check
) else (
	color 4
    echo Aborting the server installer
	goto gen_question
)

:check
if exist libraries\ (
	color 3
	echo Installation succesful
	echo Generating startup scripts
	goto gen_question
) else (
	color 4
	echo Installation not succesful
	goto end
)

:gen_question
set /p theinput="Did you want to download the start scripts? [y/n]: " 
if %theinput%==y (
	goto scripts_gen
) else (
	goto tut_question
)

:scripts_gen
:: .bat file generator
if not exist Windows.bat (
	color 3
	echo Downloading the Windows.bat
	color 7
	cd /d %FOLDER_PATH%
	curl -LJO https://raw.githubusercontent.com/lalamapaka/Tachyon/main/scripts/Windows.bat
) else (
	color 4
	echo It seems like you already have the files downloaded
	echo to download them again: could you delete Windows.bat and try this again?
)

if not exist Linux.sh (
	color 3
	echo Downloading Linux.sh
	color 7
	cd /d %FOLDER_PATH%
	curl -LJO https://raw.githubusercontent.com/lalamapaka/Tachyon/main/scripts/Linux.sh
) else (
	color 4
	echo It seems like you already have the files downloaded
	echo to download them again: could you delete Linux.sh and try this again?
)

if not exist macOS.command (
	color 3
	echo Downloading macOS.command
	color 7
	cd /d %FOLDER_PATH%
	curl -LJO https://raw.githubusercontent.com/lalamapaka/Tachyon/main/scripts/macOS.command
) else (
	color 4
	echo It seems like you already have the files downloaded
	echo to download them again: could you delete macOS.command and try this again?
	goto tutorial
)

:tut_question
set /p thisalsoaninput="Do you want to follow the tutorial again? [y/n]: " 
if %thisalsoaninput%==y (
	color 3
	echo Opening the tutorial ...
	goto tutorial
) else (
	color 4
	echo Stopping the program ...
    goto end
)


:tutorial
color 1
echo Welcome to the tutorial.
color 3
echo To stop the server while its running you have to:
color 2
echo 1. type '/stop' ingame or 'stop' in the terminal window. 
echo 2. When it asks if you realy want to stop press 'C'
color 3
echo You now would have succesfully stopped the server
echo If you want your friends to join the server from a different network
echo you have to port forward the server
color 2
echo Here you have a guide how to do that: 
echo https://www.hostinger.com/tutorials/how-to-port-forward-a-minecraft-server
goto end

:end
pause
