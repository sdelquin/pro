# Algo sobre ti 👋

1. ¿En qué te has formado hasta ahora?
2. ¿Por qué quieres estudiar DAW?
3. ¿Cuál dirías que es tu mayor virtud?
4. ¿Cuál es tu comida favorita? (_muy random_ 😜)

```python
import random

chat_done = set(int(n.strip()) for n in open('chat_done.dat'))
if not(chat_left := set(range(1, 31)) - chat_done):
    print('END❗')
else:
    pick = random.choice(list(chat_left))
    open('chat_done.dat', 'a').write(f'{pick}\n')
    print(f'Student #{pick}')
```
