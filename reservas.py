
# ==========================================
# SOFTWARE FJ
# Clase Reserva
# ==========================================

from entidades import Entidad
from clientes import Cliente
from servicios import Servicio
from excepciones import ErrorReserva, ErrorDatosInvalidos
from registro import registrar_evento, registrar_error


class Reserva(Entidad):
    """
    Clase que representa una reserva realizada
    por un cliente para un servicio.
    """

    def __init__(self, identificador, cliente, servicio, duracion):

        try:
            # Inicializar la clase padre
            super().__init__(identificador)

            # Validar que exista un cliente valido
            if not isinstance(cliente, Cliente):
                raise ErrorDatosInvalidos("El cliente no es valido.")

            # Validar que exista un servicio valido
            if not isinstance(servicio, Servicio):
                raise ErrorDatosInvalidos("El servicio no es valido.")

            # Validar la duracion
            servicio.validar_parametros(duracion)

            # Atributos privados
            self.__cliente = cliente
            self.__servicio = servicio
            self.__duracion = duracion
            self.__estado = "Pendiente"
            self.__costo = None

            registrar_evento(
                f"Reserva creada: {self.obtener_identificador()}"
            )

        except Exception as error:
            registrar_error(f"Error al crear reserva: {error}")
            raise ErrorReserva(
                "No fue posible crear la reserva."
            ) from error

    # Consultar estado
    def obtener_estado(self):
        return self.__estado

    # Consultar costo
    def obtener_costo(self):
        return self.__costo

    # Confirmar reserva
    def confirmar(self):

        try:
            if self.__estado != "Pendiente":
                raise ErrorReserva(
                    "Solo se pueden confirmar reservas pendientes."
                )

            self.__estado = "Confirmada"

            registrar_evento(
                f"Reserva confirmada: {self.obtener_identificador()}"
            )

        except ErrorReserva as error:
            registrar_error(str(error))
            raise

    # Cancelar reserva
    def cancelar(self):

        try:
            if self.__estado == "Cancelada":
                raise ErrorReserva("La reserva ya esta cancelada.")

            if self.__estado == "Procesada":
                raise ErrorReserva(
                    "No se puede cancelar una reserva procesada."
                )

            self.__estado = "Cancelada"

            registrar_evento(
                f"Reserva cancelada: {self.obtener_identificador()}"
            )

        except ErrorReserva as error:
            registrar_error(str(error))
            raise

    # Procesar reserva y calcular su costo
    def procesar(self, descuento=0, impuesto=0):

        try:
            if self.__estado != "Confirmada":
                raise ErrorReserva(
                    "La reserva debe estar confirmada para procesarse."
                )

            self.__costo = self.__servicio.calcular_costo(
                self.__duracion,
                descuento,
                impuesto
            )

        except Exception as error:
            registrar_error(f"Error al procesar reserva: {error}")
            raise ErrorReserva(
                "No fue posible procesar la reserva."
            ) from error

        else:
            self.__estado = "Procesada"

            registrar_evento(
                f"Reserva procesada correctamente: "
                f"{self.obtener_identificador()} - "
                f"Costo: {self.__costo}"
            )

            return self.__costo

        finally:
            registrar_evento(
                f"Finalizacion del intento de procesamiento: "
                f"{self.obtener_identificador()}"
            )

    # Describir reserva
    def describir(self):

        return (
            f"Reserva: {self.obtener_identificador()} | "
            f"Cliente: {self.__cliente.obtener_nombre()} | "
            f"Servicio: {self.__servicio.obtener_nombre()} | "
            f"Duracion: {self.__duracion} | "
            f"Estado: {self.__estado}"
        )
