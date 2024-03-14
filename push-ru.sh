#!/usr/bin/env bash

# copy ru-dict on the server and push on latest release in GitHub

echo -e "\033[1;33m coping ru-dict...\033[0m"

# unzip ~/Documents/dps/exporter/share/ru-pali-dictionary.zip -d ~/filesrv1/share1/Sharing\ between\ users/1\ For\ Everyone/Software/Golden\ Dictionary/Optional/

cp -rf ~/Documents/GoldenDict/ru-dpd ~/filesrv1/share1/Sharing\ between\ users/1\ For\ Everyone/Software/Golden\ Dictionary/Optional/

cp -f "/home/deva/Documents/dpd-db/dps/exporter_ru/share/ru-dpd-mdict.mdx" ~/filesrv1/share1/Sharing\ between\ users/1\ For\ Everyone/Software/MDict/ru-dpd-mdict.mdx

cp -f "/home/deva/Documents/dpd-db/dps/exporter_ru/share/ru-dpd.zip" "/home/deva/Documents/sasanarakkha/study-tools/temp-push/ru-dpd.zip"

cp -f "/home/deva/Documents/dpd-db/dps/exporter_ru/share/ru-dpd-mdict.mdx" "/home/deva/Documents/sasanarakkha/study-tools/temp-push/ru-dpd-mdict.mdx"

echo -e "\033[1;32m ru-dict moved on the server \033[0m"

cd "/home/deva/Documents/sasanarakkha/study-tools"

gh release upload --clobber 'artifacts-09.02.2024_07-04' temp-push/ru-dpd.zip

gh release upload --clobber 'artifacts-09.02.2024_07-04' temp-push/ru-dpd-mdict.mdx


echo -e "\033[1;32m ru-dict uploaded on GitHub \033[0m"
