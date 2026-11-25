
# ==========================================
# SOFTWARE FJ
# Sistema de registro de eventos y errores
# ==========================================

import logging
import os

# Crear la carpeta logs si no existe
os.makedirs("logs", exist_ok=True)

# Configurar el sistema de registro
logging.basicConfig(
    filename="logs/sistema.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8",
    force=True
)

# Obtener el registrador del sistema
logger = logging.getLogger("SoftwareFJ")


# Registrar eventos importantes
def registrar_evento(mensaje):
    logger.info(mensaje)


# Registrar errores del sistema
def registrar_error(mensaje):
    logger.error(mensaje)


# Registrar errores con informacion detallada
def registrar_error_detallado(mensaje):
    logger.exception(mensaje)
