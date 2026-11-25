
# ==========================================
# SOFTWARE FJ
# Programa principal
# ==========================================

from clientes import Cliente
from servicios import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reservas import Reserva
from registro import (
    registrar_evento,
    registrar_error_detallado
)

# ==========================================
# LISTAS INTERNAS DEL SISTEMA
# ==========================================

clientes_registrados = []
servicios_disponibles = []
reservas_registradas = []


# ==========================================
# FUNCION PARA EJECUTAR OPERACIONES
# ==========================================

def ejecutar_operacion(nombre, funcion):
    print("\n" + "=" * 55)
    print(nombre)
    print("=" * 55)

    try:
        resultado = funcion()

    except Exception as error:
        registrar_error_detallado(
            f"Fallo durante la operacion: {nombre}"
        )
        print(f"ERROR: {error}")
        return None

    else:
        registrar_evento(f"Operacion exitosa: {nombre}")
        print("Operacion realizada correctamente.")
        return resultado

    finally:
        registrar_evento(f"Finalizo la operacion: {nombre}")
        print("-" * 55)


# ==========================================
# FUNCIONES PARA REGISTRAR INFORMACION
# ==========================================

def registrar_cliente(identificador, nombre, correo, telefono):
    cliente = Cliente(identificador, nombre, correo, telefono)
    clientes_registrados.append(cliente)
    return cliente


def registrar_servicio(servicio):
    servicios_disponibles.append(servicio)
    return servicio


def registrar_reserva(reserva):
    reservas_registradas.append(reserva)
    return reserva


# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

def main():

    print("\n")
    print("=" * 55)
    print(" SISTEMA INTEGRAL DE GESTION")
    print(" CLIENTES, SERVICIOS Y RESERVAS")
    print(" SOFTWARE FJ")
    print("=" * 55)

    # --------------------------------------
    # OPERACION 1: REGISTRO DE CLIENTE VALIDO
    # --------------------------------------

    cliente1 = ejecutar_operacion(
        "OPERACION 1: Registrar cliente valido",
        lambda: registrar_cliente(
            "C001",
            "Miguel Villegas",
            "miguel@gmail.com",
            "3001234567"
        )
    )

    # --------------------------------------
    # OPERACION 2: REGISTRO DE CLIENTE INVALIDO
    # --------------------------------------

    ejecutar_operacion(
        "OPERACION 2: Intentar registrar cliente invalido",
        lambda: registrar_cliente(
            "C002",
            " ",
            "correo_incorrecto",
            "123"
        )
    )

    # --------------------------------------
    # OPERACION 3: CREAR SERVICIO DE SALA
    # --------------------------------------

    sala = ejecutar_operacion(
        "OPERACION 3: Crear servicio de reserva de sala",
        lambda: registrar_servicio(
            ReservaSala("S001", "Sala de reuniones", 50000)
        )
    )

    # --------------------------------------
    # OPERACION 4: CREAR SERVICIO DE EQUIPOS
    # --------------------------------------

    equipo = ejecutar_operacion(
        "OPERACION 4: Crear servicio de alquiler de equipos",
        lambda: registrar_servicio(
            AlquilerEquipo("S002", "Proyector", 25000)
        )
    )

    # --------------------------------------
    # OPERACION 5: CREAR SERVICIO DE ASESORIA
    # --------------------------------------

    asesoria = ejecutar_operacion(
        "OPERACION 5: Crear servicio de asesoria especializada",
        lambda: registrar_servicio(
            AsesoriaEspecializada(
                "S003",
                "Asesoria tecnologica",
                80000
            )
        )
    )

    # --------------------------------------
    # OPERACION 6: CREAR SERVICIO INVALIDO
    # --------------------------------------

    ejecutar_operacion(
        "OPERACION 6: Intentar crear servicio con tarifa invalida",
        lambda: registrar_servicio(
            ReservaSala("S004", "Sala adicional", -10000)
        )
    )

    # --------------------------------------
    # OPERACION 7: CREAR RESERVA VALIDA
    # --------------------------------------

    reserva1 = None

    if cliente1 is not None and sala is not None:
        reserva1 = ejecutar_operacion(
            "OPERACION 7: Crear reserva valida",
            lambda: registrar_reserva(
                Reserva("R001", cliente1, sala, 2)
            )
        )

    # --------------------------------------
    # OPERACION 8: CREAR RESERVA INVALIDA
    # --------------------------------------

    if cliente1 is not None and equipo is not None:
        ejecutar_operacion(
            "OPERACION 8: Intentar crear reserva con duracion invalida",
            lambda: registrar_reserva(
                Reserva("R002", cliente1, equipo, -3)
            )
        )

    # --------------------------------------
    # OPERACION 9: CONFIRMAR RESERVA
    # --------------------------------------

    if reserva1 is not None:
        ejecutar_operacion(
            "OPERACION 9: Confirmar reserva",
            lambda: reserva1.confirmar()
        )

    # --------------------------------------
    # OPERACION 10: PROCESAR RESERVA
    # --------------------------------------

    if reserva1 is not None:
        costo = ejecutar_operacion(
            "OPERACION 10: Procesar reserva y calcular costo",
            lambda: reserva1.procesar(
                descuento=10,
                impuesto=19
            )
        )

        if costo is not None:
            print(f"Costo final de la reserva: ${costo:,.2f}")

    # --------------------------------------
    # OPERACION 11: INTENTAR CANCELAR RESERVA PROCESADA
    # --------------------------------------

    if reserva1 is not None:
        ejecutar_operacion(
            "OPERACION 11: Intentar cancelar reserva procesada",
            lambda: reserva1.cancelar()
        )

    # --------------------------------------
    # OPERACION 12: CREAR Y CANCELAR OTRA RESERVA
    # --------------------------------------

    reserva2 = None

    if cliente1 is not None and asesoria is not None:
        reserva2 = ejecutar_operacion(
            "OPERACION 12: Crear segunda reserva",
            lambda: registrar_reserva(
                Reserva("R003", cliente1, asesoria, 1)
            )
        )

    if reserva2 is not None:
        ejecutar_operacion(
            "OPERACION 13: Cancelar reserva pendiente",
            lambda: reserva2.cancelar()
        )

    # ======================================
    # RESUMEN FINAL DEL SISTEMA
    # ======================================

    print("\n")
    print("=" * 55)
    print("RESUMEN DEL SISTEMA SOFTWARE FJ")
    print("=" * 55)

    print(f"Clientes registrados: {len(clientes_registrados)}")
    print(f"Servicios disponibles: {len(servicios_disponibles)}")
    print(f"Reservas registradas: {len(reservas_registradas)}")

    print("\nCLIENTES:")
    for cliente in clientes_registrados:
        print(cliente.describir())

    print("\nSERVICIOS:")
    for servicio in servicios_disponibles:
        print(servicio.describir())

    print("\nRESERVAS:")
    for reserva in reservas_registradas:
        print(reserva.describir())

    print("\n")
    print("=" * 55)
    print("FIN DE LA DEMOSTRACION")
    print("SOFTWARE FJ")
    print("=" * 55)

    registrar_evento("Finalizo la demostracion del sistema.")


# ==========================================
# INICIO DEL PROGRAMA
# ==========================================

if __name__ == "__main__":
    main()
