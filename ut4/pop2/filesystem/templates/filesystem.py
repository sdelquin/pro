class FileSystem:
    """Simulación de un sistema PLANO de ficheros tipo UNIX/Linux...
    PLANO significa que sólo se admite un nivel de directorios.

    Ejemplo:
    .
    ├── /
    │   ├── kernel.asm
    │   └── grub.sys
    ├── /etc
    │   ├── fstab.conf
    │   └── systemd.xml
    ├── /home
    │   ├── george.dat
    │   ├── john.dat
    │   ├── paul.dat
    │   └── ringo.dat
    ├── /usr
    │   ├── register.db
    │   └── web.py
    └── /var
        ├── data.txt
        ├── dmes.log
        └── info.log
    """

    # Formatos admitidos de sistemas de ficheros
    SUPPORTED_FORMATS = ('ext4', 'fat32', 'ntfs')

    def __init__(self, format: str):
        """
        Constructor de un FileSystem
        ============================
        - Habrá que crear los atributos "root" (diccionario), "cwd" (str) y "format" (str):
          → root es un diccionario que almacenará el contenido del sistema de ficheros:
            * Las claves son directorios.
            * Los valores son ficheros dentro de los directorios.
            (En un sistema "plano" → No puede haber directorios dentro de directorios)
          → cwd indica el "current work directory" o directorio actual de trabajo.
          → format indica el formato del sistema de ficheros.
        - Los formatos válidos son: 'ext4', 'fat32' y 'ntfs' (NO ES SENSIBLE A MAYÚSCULAS).
        - Si el formato no es alguno de los anteriores habrá que lanzar una excepción de
          tipo FileSystemError con el mensaje: 'Given format is not supported'
        """
        pass

    @staticmethod
    def is_directory(path: str) -> bool:
        """Comprueba si "path" es un directorio.
        Pero no lo hace a nivel del filesystem, únicamente mirando su estructura."""
        pass

    @staticmethod
    def is_file(path: str) -> bool:
        """Comprueba si "path" es un fichero.
        Pero no lo hace a nivel del filesystem, únicamente mirando su estructura."""
        pass

    @staticmethod
    def directory_required(method):
        """Este decorador comprueba si el primer argumento POSICIONAL del método decorado
        es un directorio:
        - En caso afirmativo ejecuta el método.
        - En otro caso lanza una excepción con el mensaje: 'Given path is not a directory'
        Debe hacer uso del método is_directory() definido previamente."""

        pass

    @staticmethod
    def file_required(method):
        """Este decorador comprueba si el primer argumento POSICIONAL del método decorado
        es un fichero:
        - En caso afirmativo ejecuta el método.
        - En otro caso lanza una excepción con el mensaje: 'Given path is not a file'
        Debe hacer uso del método is_file() definido previamente."""

        pass

    def __contains__(self, directory: str) -> bool:
        """Comprueba si "directory" está creado en el sistema de ficheros."""
        pass

    @directory_required
    def mkdir(self, path: str) -> None:
        """Crea un nuevo directorio en el sistema de ficheros.
        Si el directorio ya existe se debe lanzar una excepción con el mensaje:
        Directory already exists"""
        pass

    @directory_required
    def cd(self, path) -> None:
        """Cambia el directorio actual al "path" indicado.
        Si el directorio no existe debe lanzar una excepción con el mensaje:
        Directory does not exist"""
        pass

    @staticmethod
    def is_absolute_path(path: str) -> bool:
        """Indica si la ruta indicada "path" es absoluta o no,
        mirando únicamente su estructura."""
        pass

    def split_filepath(self, filepath: str) -> tuple[str, str]:
        """Divide la ruta indicada "filepath" en directorio y nombre de fichero.
        El comportamiento es distinto según "filepath" sea absoluto o relativo:
        - Si es absoluto se devolverá directorio y nombre de fichero extraído de la propia ruta.
        - Si es relativo se devolverá el directorio actual de trabajo y el nombre del fichero.
        * Ejemplo con filepath absoluto:
            /var/sys.log → ('/var', 'sys.log')
        * Ejemplo con filepath relativo:
            info.txt → (<cwd>, 'info.txt')
        Se debe hacer uso de la función is_absolute_path() definida anteriormente.
        """
        pass

    @file_required
    def touch(self, path: str) -> None:
        """Toca (o crea) un fichero (vacío) en la ruta "path".
        Si el directorio no existe debe lanzar una excepción con el mensaje:
        Directory does not exist
        Se debe hacer uso de la función split_filepath() definida anteriormente."""
        pass

    def __len__(self):
        """Calcula la longitud del sistema de ficheros.
        Esta longitud será el número de ficheros que hay en el sistema de ficheros."""
        pass

    def __str__(self):
        """Supongamos que el sistema de ficheros es 'ext4' y tenemos 21 ficheros.
        Este método debería devolver:
        ext4 filesystem with 21 files"""
        pass

    @property
    def dirs(self) -> list[str]:
        """Devuelve los directorios del sistema de ficheros ordenados alfabéticamente."""
        pass

    @property
    def files(self) -> list[str]:
        """Devuelve los ficheros del directorio actual de trabajo ordenados alfabéticamente."""
        pass

    def __iter__(self):
        """Iterador del sistema de ficheros COMO FUNCIÓN GENERADORA.
        Debe devolver todos los ficheros del sistema de ficheros (SOLO FICHEROS).
        Se debe hacer uso de los métodos dirs() y files() definidos previamente."""
        pass


class FileSystemError(Exception):
    """Clase que representa un error en el sistema de ficheros.
    - Mensaje por defecto: I/O error in filesystem
    - Si pasamos un mensaje: I/O error in filesystem: <message>"""

    def __init__(self, message: str = ''):
        pass
