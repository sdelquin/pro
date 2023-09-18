# VirtualBox

Abrimos una terminal **desde la máquina real** y ejecutamos lo siguiente:

```console
curl http://amy/daw/1daw/pro/bootstrap-pro.sh | bash
```

Ahora abrimos VirtualBox y debería aparecer una nueva máquina virtual llamada "pro". Arrancamos la máquina y entramos con estas credenciales:

- Usuario: `alu`
- Contraseña: `tranquilidad`

Abrimos una terminal **desde la máquina virtual** y ejecutamos lo siguiente:

```console
curl http://amy/daw/1daw/pro/hostname-pro.sh | bash
```

> ⚠️ Cuando nos lo solicite tendremos que poner la contraseña.

Por último cambiamos la contraseña del usuario `alu` y ponemos una nueva QUE NO SE NOS OLVIDE ejecutando el siguiente comando **en la terminal de la máquina virtual**:

```console
passwd
```
