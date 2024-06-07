# UT5-POP1: Librerías

# 🟪 PUESTO IMPAR

Esta prueba gira en torno al trabajo con **SMS** simulando su envío y recepción a través de una pequeña base de datos.

## Puesta en marcha

```console
mkdir -p ~/pro/ut5/pop1
cd ~/pro/ut5/pop1
wget https://raw.githubusercontent.com/sdelquin/pro/main/ut5/pop1/sms/templates/sms.py
wget https://raw.githubusercontent.com/sdelquin/pro/main/ut5/pop1/sms/test_sms.py
```

## Base de datos

A continuación se especifican las tablas que componen la base de datos y su estructura.

### `activity`

Representa la actividad de envío de SMS:

| Columna   | Tipo        | Descripción               |
| --------- | ----------- | ------------------------- |
| id        | Entero (PK) | Clave primaria            |
| sender    | Texto       | Teléfono del remitente    |
| recipient | Texto       | Teléfono del destinatario |
| message   | Texto       | Mensaje                   |

### `access`

Representa las credenciales de acceso al teléfono:

| Columna      | Tipo       | Descripción             |
| ------------ | ---------- | ----------------------- |
| phone_number | Texto (PK) | Número de teléfono (PK) |
| pin          | Texto      | PIN de acceso           |
| puk          | Texto      | PUK de desbloqueo       |

Ya puedes abrir tu editor favorito. ¡Suerte! 🍀
