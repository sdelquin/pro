intro:
    slides ut0/intro.md

chat:
    truncate -s 0 ut0/chat_done.dat
    cd ut0 && slides chat.md

reset:
    #!/bin/bash
    git rm -r --cached ut1/pop0
    git rm -r --cached ut1/pop1

    git rm -r --cached ut2/pop0
    git rm -r --cached ut2/pop1

    git rm -r --cached ut3/pop1
    git rm -r --cached ut3/pop2
    git rm -r --cached ut3/te1

    git rm -r --cached ut4/pop1
    git rm -r --cached ut4/pop2
    git rm -r --cached ut4/te1
    git rm -r --cached ut4/te2

    git rm -r --cached ut5/pop1
    git rm -r --cached ut5/pop2

    echo
    echo ⚠ ¡Ojo! Quitar las líneas correspondientes de .gitignore
