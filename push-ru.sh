echo "copy ru-dict"

cp -rf ~/Documents/GoldenDict/ru-pali-dictionary ~/filesrv1/share1/Sharing\ between\ users/1\ For\ Everyone/Software/Golden\ Dictionary/Optional/

cp -f "/home/deva/Documents/dps/exporter/share/ru-pali-dictionary.zip" "/home/deva/Documents/sasanarakkha/study-tools/temp-push/ru-pali-dict.zip"

echo "ru-dict moved on the server"

cd "/home/deva/Documents/sasanarakkha/study-tools"

gh release upload --clobber 'artifacts-12.04.2023_03-10-19' temp-push/ru-pali-dict.zip

echo "ru-dict uploaded on GitHub"

# echo "copy dps"

# cp -rf ~/Documents/GoldenDict/dps ~/filesrv1/share1/Sharing\ between\ users/1\ For\ Everyone/Software/Golden\ Dictionary/Optional/

# cp -f "/home/deva/Documents/dps/exporter/share/dps.zip" "/home/deva/Documents/sasanarakkha/study-tools/temp-push/dps.zip"

# echo "dps moved on the server"

# cd "/home/deva/Documents/sasanarakkha/study-tools"

# gh release upload --clobber 'artifacts-12.04.2023_03-10-19' temp-push/dps.zip

# echo "dps uploaded on GitHub"