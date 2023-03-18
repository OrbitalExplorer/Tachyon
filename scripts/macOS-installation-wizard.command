#!/bin/bash
MINECRAFT_VERSION=1.19.2
LOADER_VERSION=0.18.5
FOLDER_PATH=$(dirname "$0")
if [ ! -f "$FOLDER_PATH/usercache.json" ]; then
	echo "Getting Ready to install"
	read -p "Do You want to start the installation of the server? [y/n]: " input
	if [[ "$input" == "y" ]]; then
		echo "Downloading QUILT Installer"
		curl -LJO https://maven.quiltmc.org/repository/release/org/quiltmc/quilt-installer/latest/quilt-installer-latest.jar
		echo "Attempting to install the QUILT base server"
		java -jar quilt-installer-latest.jar install server $MINECRAFT_VERSION $LOADER_VERSION --install-dir="$FOLDER_PATH" --download-server
		if [ -d "$FOLDER_PATH/libraries" ]; then
			echo "Installation succesful"
			read -p "Did you want to download the start scripts? [y/n]: " theinput
			if [[ "$theinput" == "y" ]]; then
				if [ ! -f "$FOLDER_PATH/Windows.bat" ]; then
					echo "Downloading the Windows.bat"
					cd "$FOLDER_PATH" || exit
					curl -LJO https://raw.githubusercontent.com/lalamapaka/Tachyon/main/scripts/Windows.bat
				else
					echo "It seems like you already have the files downloaded"
					echo "To download them again: could you delete Windows.bat and try this again?"
				fi

				if [ ! -f "$FOLDER_PATH/Linux.sh" ]; then
					echo "Downloading Linux.sh"
					cd "$FOLDER_PATH" || exit
					curl -LJO https://raw.githubusercontent.com/lalamapaka/Tachyon/main/scripts/Linux.sh
					chmod +x Linux.sh
				else
					echo "It seems like you already have the files downloaded"
					echo "To download them again: could you delete Linux.sh and try this again?"
				fi

				if [ ! -f "$FOLDER_PATH/macOS.command" ]; then
					echo "Downloading macOS.command"
					cd "$FOLDER_PATH" || exit
					curl -LJO https://raw.githubusercontent.com/lalamapaka/Tachyon/main/scripts/macOS.command
					chmod +x macOS.command
				else
					echo "It seems like you already have the files downloaded"
					echo "To download them again: could you delete macOS.command and try this again?"
				fi
				read -p "Do you want to follow the tutorial again? [y/n]: " tut_input
				if [[ "$tut_input" == "y" ]]; then
					echo "Opening the tutorial ..."
					echo "Welcome to the tutorial."
					echo "To stop the server while its running you have to:"
					echo "1. Type '/stop' in-game or 'stop' in the terminal window."
					echo "2. When it asks if you really want to stop press 'C'."
					echo "You now would have successfully stopped the server."
					echo "If you want your friends to join the server from a different network, you have to port forward the server."
					echo "Here you have a guide how to do that: https://www.hostinger.com/tutorials/how-to-port-forward-a-minecraft-server"
				fi
			else
				echo "Aborting the server installer"
			fi
		fi
	else
		echo "Stopping the program ..."
	fi
fi
