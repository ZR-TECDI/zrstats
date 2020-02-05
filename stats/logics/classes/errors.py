"""Definición de errores personalizados"""

class Error(Exception):
    """Excepción base para esta app."""
    pass


class NoHayArchivo(Error):
    """Excepción que se levanta cuando no se ha definido un archivo para procesar.

    Att:
        archivo -- archivo.rpt que levantó el error
    """
    def __init__(self):
        print(f"Archivo rpt figura sin definir.")


class NoHayFecha(Error):
    """Excepción que se levanta cuando no se registra una fecha completa en el RPT.

    Att:
        rpt -- archivo.rpt que levantó el error
    """
    def __init__(self, rpt):
        self.rpt = rpt
        print(f"Ocurrió un problema al procesar {self.rpt}. ¡No tiene fecha completa!")


class NoHayRegistroAsistencia(Error):
    """Excepción que se levanta cuando no se encuentra registro en el RPT.

    Att:
        rpt -- archivo.rpt que levantó el error
    """
    def __init__(self, rpt):
        self.rpt = rpt
        print(f"Ocurrió un problema al procesar {self.rpt}. ¿Quizás no tiene registro de ZRSTATS?")


class NoHayConexion(Error):
    """Excepción que se levanta cuando un jugador no tiene evento de conexión.
    
    Att:
        jugador -- Nombre del jugador en cuestión
    
    """
    def __init__(self, jugador):
        self.jugador = jugador
        print(f"Ocurrió un problema al procesar asistencia de {jugador}. Puede no tener evento de conexión.")

class NoHayDesconexion(Error):
    """Excepción que se levanta cuando un jugador no tiene evento de desconexión.
    
    Att:
        jugador -- Nombre del jugador en cuestión
    
    """
    def __init__(self, jugador):
        self.jugador = jugador
        print(f"Ocurrió un problema al procesar asistencia de {jugador}. Puede no tener evento de desconexión.")