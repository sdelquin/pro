from __future__ import annotations


class Host:
    """Manipulación de IPs en hosts sobre redes de ordenadores.

    Excepciones
    ===========
    Todas las excepciones que se deben lanzar son de tipo IPAddressError
    cuya implementación está al final del fichero.
    """

    IPV4_BITS = 32
    # ↓ Contiene: [0, 8, 16, 24, 32]
    IPV4_SLICES = list(range(0, IPV4_BITS + 1, 8))

    def __init__(self, *args: str | int, mask: int):
        """
        Constructor de un Host
        ======================
        - Si el primer argumento de args es un string, se supondrá que es una IP en formato
          de cadena de texto.
          + Ejemplo: '192.168.1.5'
        - Si args es una tupla indica que vienen una serie de octetos de la dirección.
          + Ejemplo: (192, 168, 1, 5)
        - Si la máscara está fuera de rango habrá que elevar una excepción de dirección IP
          indicando en el mensaje: "Mask is out of range". Ejemplo: mask=33
        - Si nos pasan un número de octetos distinto de 4, habrá que elevar una excepción de
          dirección IP con el mensaje: "Only 4 octets are allowed"
        - Hay que crear los atributos "ip_octets" (tupla) y mask (entero).
          Ejemplo:
            - ip_octets = (192, 168, 1, 5)
            - mask = 24
        """
        pass

    @property
    def ip(self) -> str:
        '''Devuelve la IP del host en formato string.
        Ejemplo: "192.168.1.5"'''
        pass

    @property
    def bip(self) -> str:
        '''Devuelve la IP en formato binario. Ojo que cada octeto debe tener 8 bits.
        Ejemplo: "11000000101010000000000100000101"'''
        pass

    @property
    def addr_bmask(self) -> str:
        """Devuelve la parte de la dirección que representa la máscara (en binario).
        Ejemplo: "110000001010100000000001"
        Haz uso de la property "bip" definida anteriormente."""
        pass

    @property
    def addr_bhost(self) -> str:
        """Devuelve la parte de la dirección que representa el host (en binario).
        Ejemplo: "00000101"
        Haz uso de la property "bip" definida anteriormente."""
        pass

    @property
    def has_network_addr(self) -> bool:
        """Indica si la dirección IP corresponde con la dirección de red.
        En una dirección de red, la parte de host de la IP tiene todos los bits a 0.
        Ejemplo: "192.168.1.0"
        Haz uso de la property "addr_bhost" definida anteriormente."""
        pass

    @property
    def has_broadcast_addr(self) -> bool:
        """Indica si la dirección IP corresponde con la dirección de broadcast.
        En una dirección de broadcast, la parte de host de la IP tiene todos los bits a 1.
        Ejemplo: "192.168.1.255"
        Haz uso de la property "addr_bhost" definida anteriormente."""
        pass

    @property
    def nclass(self) -> str:
        """Devuelve la clase de la red: A, B o C.
        (no es necesario contemplar clases D y E)
        → Ver https://bit.ly/42Pgm2k
        Puedes hacer IPV4_SLICES definido anteriormente."""
        pass

    @property
    def addr_host_size(self) -> int:
        """Devuelve el número de bits que ocupa la parte de host en la dirección"""
        pass

    @property
    def num_hosts(self) -> int:
        """Devuelve el número de hosts que pueden haber en la red.
        Para calcular la cantidad de hosts por red, se usa la fórmula 2^n - 2
        donde n corresponde a la cantidad de bits para hosts."""
        pass

    def ping(self, host: Host) -> bool:
        """Indica si un host puede hacer ping a otro host.
        Para que dos hosts puedan hacer ping deben estar en la misma red."""
        pass

    def __repr__(self):
        '''Devuelve la representación del host en formato IP/Máscara.
        Ejemplo: "192.168.1.5/24"'''
        pass

    @classmethod
    def from_bip(cls, bip: str, mask: int) -> Host:
        """Crea un host a partir de una dirección IP binaria y una máscara.
        - Por ejemplo: bip='10010100101000111101010101110101' y mask=8 debería crear el host:
          148.163.213.117/8
        - Si se pasan más de 32 bits hay que lanzar una excepción de dirección incorrecta
          indicando en el mensaje: "Binary address is too long"
        """
        pass

    def __iter__(self):
        """Iterador del Host COMO FUNCIÓN GENERADORA.
        Debe devolver todos los hosts de la subred especificada por el propio host.
        Por ejemplo, para 192.168.1.45/24, habría que devolver OBJETOS DE TIPO HOST tal que:
            192.168.1.1/24
            192.168.1.2/24
            ...
            192.168.1.254/25
        Se debe hacer uso del método from_bip() definido anteriormente."""
        pass

    def __add__(self, other: Host) -> Host:
        """Suma dos objetos de tipo Host.
        El host resultante tendrá:
        - Como "IP" la suma de cada octeto correspondiente (primero con primero, segundo con segundo, etc.).
          Si la suma del octeto sobrepasa 255 se pondrá 255.
        - Como "máscara" la suma de las máscaras. Si la máscara sobrepasa 32 se pondrá 32."""
        pass


class IPAddressError(Exception):
    """Clase que representa un error en la dirección IP.
    - Mensaje por defecto: IP address is invalid
    - Si pasamos un mensaje: IP address is invalid: <message>"""

    def __init__(self, message: str = ''):
        pass
