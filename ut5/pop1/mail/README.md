# UT5-POP1: Librerías

# 🟧 PUESTO PAR

Esta prueba gira en torno al trabajo con **correos electrónicos** simulando su envío y recepción a través de una pequeña base de datos.

## Puesta en marcha

```console
mkdir -p ~/pro/ut5/pop1
cd ~/pro/ut5/pop1
wget https://raw.githubusercontent.com/sdelquin/pro/main/ut5/pop1/mail/templates/mail.py
wget https://raw.githubusercontent.com/sdelquin/pro/main/ut5/pop1/mail/test_mail.py
```

## Base de datos

A continuación se especifican las tablas que componen la base de datos y su estructura.

### `activity`

Representa la actividad de envío de correos:

| Columna   | Tipo        | Descripción             |
| --------- | ----------- | ----------------------- |
| id        | Entero (PK) | Clave primaria          |
| sender    | Texto       | Correo del remitente    |
| recipient | Texto       | Correo del destinatario |
| subject   | Texto       | Asunto                  |
| body      | Texto       | Cuerpo del correo       |

### `login`

Representa las credenciales de acceso al servidor de correo:

| Columna  | Tipo       | Descripción            |
| -------- | ---------- | ---------------------- |
| username | Texto (PK) | Nombre de usuario (PK) |
| password | Texto      | Contraseña             |
| domain   | Texto      | Dominio de correo      |

Por ejemplo, para un correo `sarah@vista.com` con contraseña `jjlogin`:

- `username` → `sarah`
- `password` → `jjlogin`
- `domain` → `vista.com`

Ya puedes abrir tu editor favorito. ¡Suerte! 🍀
