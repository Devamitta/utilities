#!/usr/bin/env bash

# generate latest vocab for all class and move it on the server and GitHub

cd "/home/deva/Documents/dpd-db/"

uv run python dps/scripts/export_from_db/save_classes_vocab_individual.py
uv run python dps/scripts/export_from_db/save_classes_vocab_united.py

cp -rf "/home/deva/Documents/sasanarakkha/study-tools/pali-class/vocab/vocab-for-classes.xlsx" "/home/deva/filesrv1/share1/Sharing between users/13 For Pāli class/vocab-for-classes.xlsx"

echo "vocab-for-classes.xlsx - done"

echo "------ pushing to git $(date) ------"

# Change to your GitHub repository directory
cd "/home/deva/Documents/sasanarakkha/study-tools"

# Get the current date
current_date=$(date +"%Y-%m-%d")

# Add all changes to the staging area
git add .

# Commit with the desired message format
commit_message="vocab $current_date"
git commit -m "$commit_message"

# Push the changes to the remote repository (GitHub)
git push

echo "------ pushing to git Ended at $(date) ------"