#!/usr/bin/env bash

# copy sbs-pd on the server and push on latest release in GitHub

echo -e "\033[1;33m coping sbs-pd...\033[0m"

cp -rf ~/Documents/GoldenDict/sbs-pd ~/filesrv1/share1/Sharing\ between\ users/1\ For\ Everyone/Software/Golden\ Dictionary/Default/

cp -f "/home/deva/Documents/dps/exporter/share/sbs-pd.zip" "/home/deva/Documents/sasanarakkha/study-tools/temp-push/sbs-pd.zip"

echo -e "\033[1;32m sbs-pd moved on the server \033[0m"

cd "/home/deva/Documents/sasanarakkha/study-tools"

gh release upload --clobber 'artifacts-17.11.2023_09-25-40' temp-push/sbs-pd.zip

echo -e "\033[1;32m sbs-pd uploaded on GitHub \033[0m"