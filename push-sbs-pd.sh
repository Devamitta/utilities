

cp -rf ~/Documents/GoldenDict/sbs-pd ~/filesrv1/share1/Sharing\ between\ users/1\ For\ Everyone/Software/Golden\ Dictionary/Default/

cp -f "/home/deva/Documents/dps/exporter/share/sbs-pd.zip" "/home/deva/Documents/sasanarakkha/study-tools/temp-push/sbs-pd.zip"

cd "/home/deva/Documents/sasanarakkha/study-tools"

gh release upload --clobber 'artifacts-08.11.2022_14-30-08' temp-push/sbs-pd.zip

echo sbs-pd uploaded