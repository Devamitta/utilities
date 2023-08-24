#!/usr/bin/env bash

# move all decks on the server and GitHub


# cd "/home/deva/Documents/dps/exporter/share"
# cp "sbs-pd.zip" "/home/deva/Documents/sasanarakkha/study-tools/temp-push/sbs-pd.zip"
# cp "ru-pali-dictionary.zip" "/home/deva/Documents/sasanarakkha/study-tools/temp-push/ru-pali-dict.zip"

# echo "SBS-PD & pali-ru-dict replased on the server"

cd "/home/deva/Documents/dps/csv-for-anki"

cp "anki-patimokkha.csv" "/home/deva/filesrv1/share1/Sharing between users/1 For Everyone/Software/Anki (learning tool)/Pāli Pātimokkha Word By Word/patimokkha-word-by-word.csv"
mv "anki-patimokkha.csv" "/home/deva/Documents/sasanarakkha/study-tools/temp-push/patimokkha-word-by-word.csv"
cp "anki-dps.csv" "/home/deva/filesrv1/share1/Sharing between users/1 For Everyone/Software/Anki (learning tool)//Пали Словарь Анки/ru-pali-vocab.csv"
mv "anki-dps.csv" "/home/deva/Documents/sasanarakkha/study-tools/temp-push/ru-pali-vocab.csv" 
cp "anki-sbs.csv" "/home/deva/filesrv1/share1/Sharing between users/1 For Everyone/Software/Anki (learning tool)/SBS Pāli-English Vocab/sbs-pd.csv"
mv "anki-sbs.csv" "/home/deva/Documents/sasanarakkha/study-tools/temp-push/sbs-pd.csv"
cp "anki-dhp.csv" "/home/deva/filesrv1/share1/Sharing between users/1 For Everyone/Software/Anki (learning tool)/Pāli DHP vocab/dhp-vocab.csv"
mv "anki-dhp.csv" "/home/deva/Documents/sasanarakkha/study-tools/temp-push/dhp-vocab.csv"
cp "anki-parittas.csv" "/home/deva/filesrv1/share1/Sharing between users/1 For Everyone/Software/Anki (learning tool)/Pāli Parittas/parittas.csv"
mv "anki-parittas.csv" "/home/deva/Documents/sasanarakkha/study-tools/temp-push/parittas.csv"


cd "/home/deva/Downloads"

cp "Pāli Pātimokkha Word By Word.apkg" "/home/deva/filesrv1/share1/Sharing between users/1 For Everyone/Software/Anki (learning tool)/Pātimokkha Word By Word/patimokkha-word-by-word.apkg"
mv "Pāli Pātimokkha Word By Word.apkg" "/home/deva/Documents/sasanarakkha/study-tools/temp-push/patimokkha-word-by-word.apkg"
cp "Пали Словарь.apkg" "/home/deva/filesrv1/share1/Sharing between users/1 For Everyone/Software/Anki (learning tool)/Пали Словарь Анки/ru-pali-vocab.apkg"
mv "Пали Словарь.apkg" "/home/deva/Documents/sasanarakkha/study-tools/temp-push/ru-pali-vocab.apkg"
cp "SBS Pāli-English Vocab.apkg" "/home/deva/filesrv1/share1/Sharing between users/1 For Everyone/Software/Anki (learning tool)/SBS Pāli-English Vocab/sbs-pali-english-vocab.apkg"
mv "SBS Pāli-English Vocab.apkg" "/home/deva/Documents/sasanarakkha/study-tools/temp-push/sbs-pali-english-vocab.apkg"
cp "DHP vocab.apkg" "/home/deva/filesrv1/share1/Sharing between users/1 For Everyone/Software/Anki (learning tool)/DHP vocab/dhp-vocab.apkg"
mv "DHP vocab.apkg" "/home/deva/Documents/sasanarakkha/study-tools/temp-push/dhp-vocab.apkg"
cp "Pāli Parittas.apkg" "/home/deva/filesrv1/share1/Sharing between users/1 For Everyone/Software/Anki (learning tool)/Parittas/parittas.apkg"
mv "Pāli Parittas.apkg" "/home/deva/Documents/sasanarakkha/study-tools/temp-push/parittas.apkg"

# cp "Ñāṇatiloka Dictionary.apkg" "/home/deva/filesrv1/share1/Sharing between users/1 For Everyone/Software/Anki (learning tool)/Ñāṇatiloka Dictionary/nanatiloka-dictionary.apkg"
# mv "Ñāṇatiloka Dictionary.apkg" "/home/deva/Documents/sasanarakkha/study-tools/temp-push/nanatiloka-dictionary.apkg"
# cp "Sutta Q&A.apkg" "/home/deva/filesrv1/share1/Sharing between users/1 For Everyone/Software/Anki (learning tool)/Sutta Q&A/sutta-q-a.apkg"
# mv "Sutta Q&A.apkg" "/home/deva/Documents/sasanarakkha/study-tools/temp-push/sutta-q-a.apkg"

# cp "/home/deva/filesrv1/share1/Sharing between users/1 For Everyone/Software/Anki (learning tool)/Reading common pali phrases/reading-common-pali-phrases.apkg" "/home/deva/Documents/sasanarakkha/study-tools/temp-push/reading-common-pali-phrases.apkg"

# cp "/home/deva/filesrv1/share1/Sharing between users/1 For Everyone/Software/Anki (learning tool)/Reading common pali phrases/reading-common-pali-phrases.csv" "/home/deva/Documents/sasanarakkha/study-tools/temp-push/reading-common-pali-phrases.csv"

echo "Anki decks and csv of SBS-PED ; PAT ; DHP ; DPS ; Pāli Parittas moved for share"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

cd "/home/deva/Documents/sasanarakkha/study-tools/temp-push"

while true; do
    read -p "push?" yn
    case $yn in
        [Yy]* ) bash github-assets-uploader.sh; break;;
        [Nn]* ) exit;;
        *  ) echo "only yes or no";;
    esac
done

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "the job is done"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "please change all artifacts in dps via VSCode"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
