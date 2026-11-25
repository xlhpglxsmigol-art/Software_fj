
# ==========================================
# SOFTWARE FJ
# Clase Cliente
# ==========================================

import re
from entidades import Entidad
from excepciones import ErrorCliente, ErrorDatosInvalidos
from registro import registrar_evento, registrar_error


class Cliente(Entidad):
    """
    Clase que representa a los clientes de Software FJ.
    Hereda de la clase abstracta Entidad.
    """

    def __init__(self, identificador, nombre, correo, telefono):
        try:
            # Inicializar la clase padre
            super().__init__(identificador)

            # Validar nombre
            if not isinstance(nombre, str) or not nombre.strip():
                raise ErrorDatosInvalidos("El nombre no puede estar vacio.")

            # Validar correo electronico
            if not isinstance(correo, str) or not re.fullmatch(
                r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
                correo.strip()
            ):
                raise ErrorDatosInvalidos("El correo electronico no es valido.")

            # Validar telefono
            if not isinstance(telefono, str) or not re.fullmatch(
                r"\+?[0-9]{7,15}", telefono.strip()
            ):
                raise ErrorDatosInvalidos("El telefono no es valido.")

            # Atributos privados (encapsulacion)
            self.__nombre = nombre.strip()
            self.__correo = correo.strip()
            self.__telefono = telefono.strip()

            registrar_evento(
                f"Cliente registrado correctamente: {self.obtener_identificador()}"
            )

        except ErrorDatosInvalidos as error:
            registrar_error(f"Error al crear cliente: {error}")
            raise ErrorCliente("No fue posible registrar el cliente.") from error

        except Exception as error:
            registrar_error(f"Error inesperado al crear cliente: {error}")
            raise ErrorCliente("Ocurrio un error inesperado.") from error

    # Consultar nombre
    def obtener_nombre(self):
        return self.__nombre

    # Consultar correo
    def obtener_correo(self):
        return self.__correo

    # Consultar telefono
    def obtener_telefono(self):
        return self.__telefono

    # Modificar correo con validacion
    def cambiar_correo(self, nuevo_correo):
        if not isinstance(nuevo_correo, str) or not re.fullmatch(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            nuevo_correo.strip()
        ):
            raise ErrorDatosInvalidos("El nuevo correo no es valido.")

        self.__correo = nuevo_correo.strip()
        registrar_evento(
            f"Correo actualizado para el cliente: {self.obtener_identificador()}"
        )

    # Describir cliente (polimorfismo)
    def describir(self):
        return (
            f"Cliente: {self.__nombre} | "
            f"Correo: {self.__correo} | "
            f"Telefono: {self.__telefono}"
        )
