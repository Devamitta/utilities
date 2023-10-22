#!/usr/bin/env bash

# all left bash (the rest in dpd-db/dps/bash)

echo -e "\033[1;33m We are going to make various csv and push decks on the server. \033[0m"

cd "/home/deva/Documents/dps/patimokkha_dict"

# Pātimokkha ODS - https://docs.google.com/spreadsheets/d/1rS-IlX4DvKmnBO58KON37eVnOZqwfkG-ot-zIjCuzH4/

while true; do
    echo -e "\033[1;36m please download the latest Pātimokkha ODS! \033[0m"
    echo -ne "\033[1;34m need to generate patimokkha.csv? \033[0m"
    read yn
    case $yn in
        [Yy]* )
            echo -e "\033[1;33m generating patimokkha.csv...\033[0m"
            bash makecsv.sh
            break;;
        [Nn]* )
            break;;
        *  )
            echo -e "\033[1;31m Please enter only yes or no\033[0m";;
    esac
done

cd "/home/deva/Downloads"

mv -f "grammar.xlsx" "/home/deva/Documents/dps/pāli-course/grammar.xlsx"

cd "/home/deva/Documents/dps/utilities"

# grammar.xlsx - https://docs.google.com/spreadsheets/d/1KV5LmebIQpNyNKl03Pmo_Ti-LNW3IYWB6uc7OfGRGPU/

while true; do
    echo -e "\033[1;36m please download the latest grammar.xlsx! \033[0m"
    echo -ne "\033[1;34m need to make updated grammar.csv? \033[0m"
    read yn
    case $yn in
        [Yy]* )
            echo -e "\033[1;33m generating grammar.csv...\033[0m"
            poetry run python anki_class_grammar.py
            break;;
        [Nn]* )
            break;;
        *  )
            echo -e "\033[1;31m Please enter only yes or no\033[0m";;
    esac
done


while true; do
    echo -e "\033[1;36m please save all class anki decks! \033[0m"
    echo -ne "\033[1;34m need to move all classes? \033[0m"
    read yn
    case $yn in
        [Yy]* )
            echo -e "\033[1;33m moving all classes...\033[0m"
            bash move-class.sh
            break;;
        [Nn]* )
            break;;
        *  )
            echo -e "\033[1;31m Please enter only yes or no\033[0m";;
    esac
done

while true; do
    echo -e "\033[1;36m please save all other anki decks! \033[0m"
    echo -ne "\033[1;34m need to move all other decks? \033[0m"
    read yn
    case $yn in
        [Yy]* )
            echo -e "\033[1;33m moving all other decks...\033[0m"
            bash move-decks.sh
            break;;
        [Nn]* )
            break;;
        *  )
            echo -e "\033[1;31m Please enter only yes or no\033[0m";;
    esac
done


cd "/home/deva"

while true; do
    echo -ne "\033[1;34m need to open dpd-db.code-workspace? \033[0m"
    read yn
    case $yn in
        [Yy]* )
            echo -e "\033[1;33m opening dpd-db.code-workspace...\033[0m"
            code dpd-db.code-workspace
            break;;
        [Nn]* )
            break;;
        *  )
            echo -e "\033[1;31m Please enter only yes or no\033[0m";;
    esac
done

cd "/home/deva/Documents/dps/utilities"

while true; do
    echo -ne "\033[1;34m need to open study-tools-releases.html? \033[0m"
    read yn
    case $yn in
        [Yy]* )
            echo -e "\033[1;33m opening releases page...\033[0m"
            google-chrome study-tools-releases.html
            break;;
        [Nn]* )
            break;;
        *  )
            echo -e "\033[1;31m Please enter only yes or no\033[0m";;
    esac
done


echo -e "\033[1;32m what have to be done has been done! \033[0m"

echo -e "\033[1;32m ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \033[0m"