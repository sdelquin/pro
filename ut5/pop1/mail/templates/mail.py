import re
import sqlite3

DB_PATH = 'mail.db'

"""
Diagrama de clases:

            +-----------+                       +-----------+
            |           |                       |           |
      +-----+ DBHandler +------+                | MailError |
      |     |           |      |                |           |
      |     +-----------+      |                +-----------+
      |                        |                             
      |                        |                             
      |                        |                             
      v                        v                             
+------------+         +--------------+                      
|            |         |              |                      
|    Mail    |         |  MailServer  |                      
|            |         |              |                      
+------------+         +--------------+                      
"""


class DbHandler:
    def __init__(self, db_path: str = DB_PATH):
        """Crea la conexión a la base de datos (factoría Row) y el cursor correspondiente.
        También crea atributos homónimos a parámetros"""
        pass

    def create_db(self) -> None:
        """Crea la base de datos y sus tablas"""
        pass


class Mail(DbHandler):
    """Clase que representa un correo electrónico."""

    def __init__(self, sender: str, recipient: str, subject: str, body: str):
        """Construye un objeto Mail con los mismos atributos que parámetros.
        Esta clase hereda de DbHandler...

        NO HAY QUE ALMACENAR NADA EN LA BASE DE DATOS"""
        pass

    def send(self) -> None:
        """Simula el envío de este correo (self) guardando todos sus campos en la tabla activity"""
        pass

    def __str__(self):
        """Representa un objeto de tipo Mail de la siguiente forma:
        From: <remitente>
        To: <destinatario>
        ---
        <asunto pasado a mayúsculas>
        <cuerpo del correo>
        """
        pass


class MailServer(DbHandler):
    """Clase que representa un SERVIDOR DE CORREO."""

    def __init__(self, username: str):
        """Construye un MailServer creando el atributo de nombre de usuario.
        También es necesario crear un atributo logged (booleano) que indique si se ha logeado.
        Esta clase hereda de DbHandler..."""
        pass

    def login(self, password: str) -> None:
        """Intenta hacer el login del usuario comprobando con la contraseña que se pasa.
        También hay que ACTUALIZAR los atributos del objeto: "domain" y "logged".
        → La comprobación hay que hacerla consultando la base de datos.
        Notas:
          + Si el usuario se logea correctamente, su dominio será el que está almacenado en la
            base de datos.
          + Si el usuario no se logea correctamente, su dominio será la cadena vacía.
        """
        pass

    @staticmethod
    def login_required(method):
        """Decorador que lanza una excepción MailError si el usuario no está logeado.
        El mensaje de la excepción debe ser:
        User "<username>" not logged in!

        Ojo! La excepción recibe en su constructor tanto el mensaje de error
        como el objeto actual de tipo MailServer."""

        pass

    @property
    def sender(self) -> str:
        """Formato: <nombre-de-usuario>@<dominio>

        No hay que aplicar decorador pero debes saber que esta propiedad
        sólo va a funcionar si se ha hecho login previamente, ya que en otro caso
        no disponemos del dominio."""
        pass

    @login_required
    def send_mail(self, *, recipient: str, subject: str, body: str) -> None:
        """Realiza el "envío" de un correo a través de un objeto de tipo Mail.
        Si recipient no tiene un formato válido de email se debe lanzar una excepción
        de tipo MailError con el mensaje:
        Recipient "<recipient>" has invalid mail format!

        Ojo! La excepción recibe en el constructor tanto el mensaje
        como el objeto actual de tipo MailServer."""
        pass

    @login_required
    def get_emails(self, sent: bool = True):
        """FUNCIÓN GENERADORA que devuelve objetos de tipo Mail.
        - Si el parámetro "sent" es True se devuelven los enviados por el usuario.
        - Si el parámetro "sent" es False se devuelven los recibidos por el usuario."""
        pass


class MailError(Exception):
    def __init__(self, message: str, mail_handler: Mail | MailServer):
        """Hay que cerrar la conexión a la base de datos"""
        pass
