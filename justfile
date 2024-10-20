# https://github.com/maaslalani/slides
# CTRL-E para ejecutar el trozo de código
@intro:
    truncate -s 0 ut0/intro_done.dat
    cd ut0 && slides intro.md

# Resetear el repositorio (principio de curso)
# https://stackoverflow.com/a/26000395
[confirm('Borrar todo el historial de git? [y/n]')]
reset:
    #!/usr/bin/env bash
    git checkout --orphan latest_branch
    git add -A
    git commit -am "New school year"
    git branch -D main
    git branch -m main
    git push --set-upstream -f origin main

    echo
    echo ⚠ ¡Ojo! Quitar las líneas correspondientes de .gitignore

[no-cd]
coverage:
    pytest --cov --cov-report=html

# Renderizar (y expandir) el howto para todas las POP
expand-howto:
    python management/howto.py
