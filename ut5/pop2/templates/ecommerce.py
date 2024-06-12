from __future__ import annotations

import re
import sqlite3

DB_PATH = 'ecommerce.db'

# ************************************************************
# Usuario
# ************************************************************


def create_db(db_path: str):
    """Crea la base de datos en la ruta db_path
    Recuerda que la tabla "cart" tiene claves ajenas a "user" y "product"
    """
    pass


class User:
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    def __init__(self, username: str, name: str, surname: str, id: int = None):
        """Comprueba que el username siga el siguiente patrón (usando regex):
        - Empezar con una letra minúscula.
        - Terminar con un dígito.
        - Estar formado por letras, números y guiones bajos.
        - Tener un mínimo de 8 caracteres.
        Si no sigue este patrón, hay que elevar una excepción ValueError con el
        mensaje: User "<username>" does not follow security rules!

        A continuación guarda los atributos pasados por parámetro."""
        pass

    def save(self) -> None:
        """Almacena el objeto actual en la base de datos y actualiza el
        identificador del objeto desde la base de datos."""
        pass

    def update(self) -> None:
        """Actualiza todos los campos del objeto en la base de datos usando
        el identificador como referencia.
        Si el objeto aún no se ha guardado en la base de datos, lanza una excepción de tipo
        ValueError con el mensaje: User "<username>" has not been yet saved into DB!"""
        pass

    def __str__(self):
        """Representación en formato:
        <name> <surname>"""
        pass

    @classmethod
    def from_id(cls, user_id: int) -> User:
        """Construye un objeto User a partir del identificador de usuario consultando
        la base de datos.
        Si el identificador de usuario no existe hay que lanzar una excepción de tipo
        ValueError con el mensaje: User with id <user_id> does not exist in DB!"""
        pass


# ************************************************************
# Producto
# ************************************************************


class Product:
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    def __init__(self, name: str, stock: int, price: float, id: int = None):
        """Construye el objeto creando atributos homónimos a los parámetros."""
        pass

    def save(self) -> None:
        """Almacena el objeto actual en la base de datos y actualiza el
        identificador del objeto desde la base de datos."""
        pass

    def update(self) -> None:
        """Actualiza todos los campos del objeto en la base de datos usando
        el identificador como referencia.
        Si el objeto aún no se ha guardado en la base de datos, lanza una excepción de tipo
        ValueError con el mensaje: Product "<nombre-producto>" has not been yet saved into DB!"""
        pass

    def sell(self, qty: int) -> None:
        """Si la cantidad a vender es mayor que el stock hay que lanzar una excepción de tipo
        ValueError con el mensaje: Not enough stock for product "<nombre-producto>!"
        Si todo ha ido bien hay que actualizar el atributo de stock del objeto y actualizar
        la información del objeto en la base de datos."""
        pass

    def restock(self, qty: int) -> None:
        """Actualiza el atributo stock del objeto según corresponda y actualiza la información
        del objeto en la base de datos.
        Haz uso de métodos ya implementados."""
        pass

    def __str__(self):
        """El producto se representa por su nombre."""
        pass

    def __eq__(self, other: Product | object):
        """Comprueba que dos productos son iguales únicamente a través de su nombre."""
        pass

    @classmethod
    def from_id(cls, product_id: int) -> Product:
        """Construye un objeto Product a partir del identificador de producto consultando
        la base de datos.
        Si el identificador de producto no existe hay que lanzar una excepción de tipo
        ValueError con el mensaje: Product with id <product_id> does not exist in DB!"""
        pass


# ************************************************************
# Carrito
# ************************************************************


class Cart:
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    @classmethod
    def purchase(cls, user_id: int, product_id: int, qty: int) -> None:
        """El usuario compra qty unidades de producto.
        Esto implica que hay que actualizar el stock del producto así como añadir
        una nueva fila en la tabla "cart" con la operación.
        Aprovecha métodos ya definidos en las clases anteriores para algunas de las
        partes que debes implementar."""
        pass

    @classmethod
    def clean(cls, user_id: int) -> None:
        """Vaciar el carrito de la compra.
        Hay que actualizar el stock de los productos que había en el carrito
        así como eliminar los productos en sí mismos del carrito.
        Aprovecha métodos ya definidos en las clases anteriores para algunas de las
        partes que debes implementar."""
        pass
