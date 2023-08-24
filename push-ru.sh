#!/usr/bin/env bash

# copy ru-dict on the server and poush on latest release in GitHub

echo "coping ru-dict"

cp -rf ~/Documents/GoldenDict/ru-pali-dictionary ~/filesrv1/share1/Sharing\ between\ users/1\ For\ Everyone/Software/Golden\ Dictionary/Optional/

cp -f "/home/deva/Documents/dps/exporter/share/ru-pali-dictionary.zip" "/home/deva/Documents/sasanarakkha/study-tools/temp-push/ru-pali-dict.zip"

echo "ru-dict moved on the server"

cd "/home/deva/Documents/sasanarakkha/study-tools"

gh release upload --clobber 'artifacts-02.08.2023_08-23-46' temp-push/ru-pali-dict.zip

echo "ru-dict uploaded on GitHub"