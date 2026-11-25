
# ==========================================
# SOFTWARE FJ
# Clase abstracta Servicio y servicios derivados
# ==========================================

from abc import ABC, abstractmethod
from excepciones import ErrorServicio, ErrorDatosInvalidos
from registro import registrar_evento, registrar_error


class Servicio(ABC):
    """
    Clase abstracta que representa los servicios
    ofrecidos por la empresa Software FJ.
    """

    def __init__(self, identificador, nombre, tarifa_base):
        try:
            if not identificador or not str(identificador).strip():
                raise ErrorDatosInvalidos("El identificador es obligatorio.")

            if not nombre or not isinstance(nombre, str) or not nombre.strip():
                raise ErrorDatosInvalidos("El nombre del servicio es obligatorio.")

            if isinstance(tarifa_base, bool) or not isinstance(tarifa_base, (int, float)) or tarifa_base <= 0:
                raise ErrorDatosInvalidos("La tarifa debe ser un numero mayor que cero.")

            # Atributos privados
            self.__identificador = str(identificador).strip()
            self.__nombre = nombre.strip()
            self.__tarifa_base = float(tarifa_base)

        except ErrorDatosInvalidos as error:
            registrar_error(f"Error al crear servicio: {error}")
            raise ErrorServicio("No fue posible crear el servicio.") from error

    def obtener_identificador(self):
        return self.__identificador

    def obtener_nombre(self):
        return self.__nombre

    def obtener_tarifa(self):
        return self.__tarifa_base

    @abstractmethod
    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        pass

    @abstractmethod
    def describir(self):
        pass

    @abstractmethod
    def validar_parametros(self, duracion):
        pass


# ==========================================
# SERVICIO 1: RESERVA DE SALAS
# ==========================================

class ReservaSala(Servicio):

    def validar_parametros(self, duracion):
        if isinstance(duracion, bool) or not isinstance(duracion, (int, float)) or duracion <= 0:
            raise ErrorDatosInvalidos("La duracion de la reserva debe ser mayor que cero.")

    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        self.validar_parametros(duracion)

        if not 0 <= descuento <= 100 or not 0 <= impuesto <= 100:
            raise ErrorDatosInvalidos("El descuento y el impuesto deben estar entre 0 y 100.")

        subtotal = self.obtener_tarifa() * duracion
        total = subtotal - (subtotal * descuento / 100)
        total += total * impuesto / 100

        return round(total, 2)

    def describir(self):
        return f"Reserva de sala: {self.obtener_nombre()}"


# ==========================================
# SERVICIO 2: ALQUILER DE EQUIPOS
# ==========================================

class AlquilerEquipo(Servicio):

    def validar_parametros(self, duracion):
        if isinstance(duracion, bool) or not isinstance(duracion, (int, float)) or duracion <= 0:
            raise ErrorDatosInvalidos("Las horas de alquiler deben ser mayores que cero.")

    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        self.validar_parametros(duracion)

        if not 0 <= descuento <= 100 or not 0 <= impuesto <= 100:
            raise ErrorDatosInvalidos("El descuento y el impuesto deben estar entre 0 y 100.")

        subtotal = self.obtener_tarifa() * duracion
        total = subtotal - (subtotal * descuento / 100)
        total += total * impuesto / 100

        return round(total, 2)

    def describir(self):
        return f"Alquiler de equipo: {self.obtener_nombre()}"


# ==========================================
# SERVICIO 3: ASESORIAS ESPECIALIZADAS
# ==========================================

class AsesoriaEspecializada(Servicio):

    def validar_parametros(self, duracion):
        if isinstance(duracion, bool) or not isinstance(duracion, (int, float)) or duracion <= 0:
            raise ErrorDatosInvalidos("La duracion de la asesoria debe ser mayor que cero.")

    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        self.validar_parametros(duracion)

        if not 0 <= descuento <= 100 or not 0 <= impuesto <= 100:
            raise ErrorDatosInvalidos("El descuento y el impuesto deben estar entre 0 y 100.")

        subtotal = self.obtener_tarifa() * duracion
        total = subtotal - (subtotal * descuento / 100)
        total += total * impuesto / 100

        return round(total, 2)

    def describir(self):
        return f"Asesoria especializada: {self.obtener_nombre()}"
