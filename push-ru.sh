cp -rf ~/Documents/GoldenDict/ru-pali-dictionary ~/filesrv1/share1/Sharing\ between\ users/1\ For\ Everyone/Software/Golden\ Dictionary/Optional/

cp -f "/home/deva/Documents/dps/exporter/share/ru-pali-dictionary.zip" "/home/deva/Documents/sasanarakkha/study-tools/temp-push/ru-pali-dict.zip"

cd "/home/deva/Documents/sasanarakkha/study-tools"

gh release upload --clobber 'artifacts-15.12.2022_10-34-00' temp-push/ru-pali-dict.zip

echo ru-dict uploaded