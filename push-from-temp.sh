#!/usr/bin/env bash

# push (somthing from temp) on latest release in GitHub

cd "/home/deva/Documents/sasanarakkha/study-tools/temp-push"

# Print current working directory
echo "Current working directory: $(pwd)"

# List files in the current directory
echo "Files in the directory:"
ls

# Prompt the user for input
read -p "Enter the full filename (including extension): " filename

# Check if the user provided an argument
if [ -z "$filename" ]; then
  echo "Filename cannot be empty. Exiting."
  exit 1
fi

# Ensure the file exists before attempting to upload
if [ ! -e "$filename" ]; then
  echo "File '$filename' does not exist. Exiting."
  exit 1
fi

gh release upload --clobber "artifacts-09.02.2024_07-04 " "$filename"

