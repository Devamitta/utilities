#!/usr/bin/env bash

# all left bash (the rest in dpd-db/dps/bash)


cd "/home/deva/Documents/dps/patimokkha_dict"

while true; do
    read -p "neeed to generate patimokkha.csv? please download the latest Pātimokkha ODS!" yn
    case $yn in
        [Yy]* ) bash makecsv.sh; break;;
        [Nn]* ) break;;
        *  ) echo "only yes or no";;
    esac
done

cd "/home/deva/Downloads"

mv -f "grammar.xlsx" "/home/deva/Documents/dps/pāli-course/grammar.xlsx"

cd "/home/deva/Documents/dps/utilities"


while true; do
    read -p "need to make upadted grammar.csv?" yn
    case $yn in
        [Yy]* ) poetry run python anki_class_grammar.py ; break;;
        [Nn]* ) break;;
        *  ) echo "only yes or no";;
    esac
done

while true; do
    read -p "need to move all classes? please save all class anki decks." yn
    case $yn in
        [Yy]* ) bash move-class.sh; break;;
        [Nn]* ) break;;
        *  ) echo "only yes or no";;
    esac
done

while true; do
    read -p "need to move all decks? please save all anki decks." yn
    case $yn in
        [Yy]* ) bash move-decks.sh; break;;
        [Nn]* ) break;;
        *  ) echo "only yes or no";;
    esac
done

cd "/home/deva"

while true; do
    read -p "open sbs.code-workspace" yn
    case $yn in
        [Yy]* ) code sbs.code-workspace; break;;
        [Nn]* ) break;;
        *  ) echo "only yes or no";;
    esac
done

while true; do
    read -p "open dpd-db.code-workspace" yn
    case $yn in
        [Yy]* ) code dpd-db.code-workspace; break;;
        [Nn]* ) break;;
        *  ) echo "only yes or no";;
    esac
done

cd "/home/deva/Documents/dps/utilities"

while true; do
    read -p "open google-chrome study-tools-releases.html" yn
    case $yn in
        [Yy]* ) google-chrome study-tools-releases.html; break;;
        [Nn]* ) break;;
        *  ) echo "only yes or no";;
    esac
done


echo -e "\033[34mdone\033[0m"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"