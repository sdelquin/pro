# UT1-POP1-EJ3
VOWELS = 'aeiou'
target_vowel = 'e'
target_offset = 2
input_text = 'Hay una gran diferencia entre conocer el camino y andar el camino'
# No tocar nada de aquí hacia arriba ↑
# ********************************************************

# ========================================================
# @@ Escribe tu código debajo de esta línea ↓

target_vowel_index = VOWELS.index(target_vowel)
offset_vowel_index = target_vowel_index + target_offset
offset_vowel = VOWELS[offset_vowel_index]
output_text = input_text.replace(target_vowel, offset_vowel)

# $$ Escribe tu código encima de esta línea ↑
# ========================================================

# ********************************************************
# No tocar nada de aquí hacia abajo ↓
assert output_text == 'Hay una gran diforoncia ontro conocor ol camino y andar ol camino'
