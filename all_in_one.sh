#!/usr/bin/env bash

# all for update of sbs-study-tools (https://sasanarakkha.github.io/study-tools/)

echo -e "\033[1;33m We are going to make various csv and push decks on the server. \033[0m"

cd '/home/deva/.local/bin'

while true; do
    echo -ne "\033[1;34m need to make latest csv for anki? \033[0m"
    read yn
    case $yn in
        [Yy]* )
            bash anki.sh
            break;;
        * )
            break;;
    esac
done


cd "/home/deva/Documents/dps/utilities"

while true; do
    echo -ne "\033[1;34m need to push vocab for classes? \033[0m"
    read yn
    case $yn in
        [Yy]* )
            echo -e "\033[1;33m pushing vocab for classes...\033[0m"
            bash generate_and_push_vocab.sh
            break;;
        * )
            break;;
    esac
done

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
        * )
            break;;
    esac
done

cd "/home/deva/Documents/dps/patimokkha_dict"

# Pātimokkha ODS - https://docs.google.com/spreadsheets/d/1rS-IlX4DvKmnBO58KON37eVnOZqwfkG-ot-zIjCuzH4/

while true; do
    echo -e "\033[1;36m please download the latest Pātimokkha XLSX! \033[0m"
    echo -ne "\033[1;34m need to generate patimokkha.csv? \033[0m"
    read yn
    case $yn in
        [Yy]* )
            echo -e "\033[1;33m generating patimokkha.csv...\033[0m"
            bash make_pat.sh
            break;;
        * )
            break;;
    esac
done

cd "/home/deva/Documents/dps/utilities"

while true; do
    echo -e "\033[1;36m please save all class anki decks! \033[0m"
    echo -ne "\033[1;34m need to move all classes? \033[0m"
    read yn
    case $yn in
        [Yy]* )
            echo -e "\033[1;33m moving all classes...\033[0m"
            bash move-class.sh
            break;;
        * )
            break;;
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
        * )
            break;;
    esac
done

while true; do
    echo -ne "\033[1;34m need to push individually on GitHub? \033[0m"
    read yn
    case $yn in
        [Yy]* )
            echo -e "\033[1;33m pushing all...\033[0m"
            bash push-from-temp.sh
            ;;
        * )
            break;;
    esac

    # Ask if the user wants to repeat
    echo -ne "\033[1;34m repeat? \033[0m"
    read repeat
    case $repeat in
        [Yy]* )
            continue;;
        * )
            break;;
    esac
done


cd "/home/deva/Documents/sasanarakkha/study-tools/temp-push"

while true; do
    echo -ne "\033[1;34m need to push on GitHub? \033[0m"
    read yn
    case $yn in
        [Yy]* )
            echo -e "\033[1;33m pushing all...\033[0m"
            bash github-assets-uploader.sh
            break;;
        *  )
            break;;
    esac
done

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "please change all artifacts in dps via VSCode"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"


# cd "/home/deva/Documents"

# while true; do
#     echo -ne "\033[1;34m need to open dps.code-workspace? \033[0m"
#     read yn
#     case $yn in
#         [Yy]* )
#             echo -e "\033[1;33m opening dps.code-workspace...\033[0m"
#             code dps.code-workspace &
#             break;;
#         * )
#             break;;
#     esac
# done

# cd "/home/deva/Documents/sasanarakkha/study-tools"

# bash replace-latest-release.sh

# while true; do
#     echo -ne "\033[1;34m need to open study-tools-releases.html? \033[0m"
#     read yn
#     case $yn in
#         [Yy]* )
#             echo -e "\033[1;33m opening releases page...\033[0m"
#             firefox study-tools-releases.html &
#             break;;
#         * )
#             break;;
#     esac
# done


echo -e "\033[1;32m what have to be done has been done! \033[0m"

echo -e "\033[1;32m ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \033[0m"