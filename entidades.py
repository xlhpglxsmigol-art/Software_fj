
# ==========================================
# SOFTWARE FJ
# Clase abstracta Entidad
# ==========================================

from abc import ABC, abstractmethod


class Entidad(ABC):
    """
    Clase abstracta que representa las entidades
    generales del sistema Software FJ.
    """

    def __init__(self, identificador):
        # Validar que el identificador no este vacio
        if not identificador or not str(identificador).strip():
            raise ValueError("El identificador no puede estar vacio.")

        # Atributo encapsulado
        self.__identificador = str(identificador).strip()

    # Metodo para consultar el identificador
    def obtener_identificador(self):
        return self.__identificador

    # Metodo abstracto para describir una entidad
    @abstractmethod
    def describir(self):
        pass
