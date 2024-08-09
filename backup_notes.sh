#!/bin/bash

exec > >(tee "/home/deva/logs/backup_notes.log") 2>&1

echo "------ backup_notes Script Started at $(date) ------"

# Get the current date
current_date=$(date +"%Y-%m-%d")

# Change to your GitHub repository directory
cd Documents/note/

# Add all changes to the staging area
git add .

# Commit with the desired message format
commit_message="backup $current_date"
git commit -m "$commit_message"

# Push the changes to the remote repository (GitHub)
git push

echo "------ backup_notes Script Ended at $(date) ------"



# export VISUAL=xed; crontab -e 