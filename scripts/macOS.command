#!/bin/bash
while true; do
    java -Xmx3G -Xms3G -jar quilt-server-launch.jar nogui
    t=10
    while [ $t -gt 0 ]; do
        clear
        echo "Restart in $t seconds, press C to cancel: "
        read -t 1 -n 1 key
        if [[ $key == c ]]; then
            echo "You cancelled shutdown"
            exit 0
        fi
        t=$((t-1))
    done
    echo "Restarting down"
