cp -rf ~/Documents/GoldenDict/ru-pali-dictionary ~/filesrv1/share1/Sharing\ between\ users/1\ For\ Everyone/Software/Golden\ Dictionary/Optional/

cp -f "/home/deva/Documents/dps/exporter/share/ru-pali-dictionary.zip" "/home/deva/Documents/sasanarakkha/study-tools/temp-push/ru-pali-dict.zip"

cd "/home/deva/Documents/sasanarakkha/study-tools"

gh release upload --clobber 'artifacts-08.11.2022_14-30-08' temp-push/ru-pali-dict.zip

echo ru-dict uploaded