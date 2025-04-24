#!/bin/bash

exec > >(tee "/home/deva/logs/backup_filesrv.log") 2>&1

echo "------ backup_filesrv Script Started at $(date) ------"

# Check if the directory is not mounted
if ! grep -qs '/home/deva/filesrv1/share1' /proc/mounts; then
    # Try to mount it. If mounting fails, exit.
    if ! mount /home/deva/filesrv1/share1; then
        echo "Failed to mount /home/deva/filesrv1/share1. Exiting."
        exit 1
    else
        echo "Mounted /home/deva/filesrv1/share1"
    fi
else 
    echo "/home/deva/filesrv1/share1 is mounted already"    
fi

rsync -azxi --no-links --exclude-from='/home/deva/Documents/dps/utilities/.rsync-exclude' --info=progress2 --stats /home/deva/Audio /home/deva/Videos /home/deva/Camera /home/deva/Pictures /home/deva/Documents /home/deva/backups /home/deva/logs "/home/deva/filesrv1/share1/devamitta/"

echo "------ backup_filesrv Script Ended at $(date) ------"


# export VISUAL=xed; crontab -e 