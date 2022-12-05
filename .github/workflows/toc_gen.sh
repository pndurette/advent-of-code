# /bin/bash

# Clear README.md after marker
sed -i '/<!-- table of contents generated below -->/q' README.md

# Find directories that start with 20* (i.e year), sorted
# e.g.: 2022, 2022/day1, 2022/day1/python, 2022/day2, 2022/day2/python, ...
for dir in $(find 20* -maxdepth 3 -type d | sort -V); do
    # Split the <dir> path into <year>/<dayn>/<lang> variables
    arrParts=(${dir//\// })

    YEAR=${arrParts[0]}
    DAYN=${arrParts[1]}
    LANG=${arrParts[2]}

    # If there's no day, it's a year; if there's no lang, it's a day.
    [[ "$DAYN" = "" ]] && printf "\n## [$YEAR]($YEAR)" >> README.md && continue
    [[ "$LANG" = "" ]] && printf "\n* [$DAYN]($dir): " >> README.md && continue
    printf "[[$LANG]($dir)] " >> README.md
done