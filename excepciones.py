
# ==========================================
# SOFTWARE FJ
# Manejo de excepciones personalizadas
# ==========================================

# Clase base para los errores del sistema
class ErrorSistema(Exception):
    """Excepcion general del sistema Software FJ."""
    pass


# Error cuando los datos de un cliente son incorrectos
class ErrorCliente(ErrorSistema):
    """Error relacionado con los datos del cliente."""
    pass


# Error cuando un servicio no esta disponible
class ErrorServicio(ErrorSistema):
    """Error relacionado con los servicios."""
    pass


# Error cuando una reserva presenta problemas
class ErrorReserva(ErrorSistema):
    """Error relacionado con las reservas."""
    pass


# Error cuando se ingresan datos invalidos
class ErrorDatosInvalidos(ErrorSistema):
    """Error cuando los datos ingresados no son validos."""
    pass


# Error cuando una operacion no esta permitida
class ErrorOperacion(ErrorSistema):
    """Error cuando se intenta realizar una operacion no permitida."""
    pass
