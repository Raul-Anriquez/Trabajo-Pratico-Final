import functools
import datetime
import time
from typing import Any, Callable

#LOG DE AUDITORIA

_log_auditoria = []

def _serializar(obj):
    if obj is None:
        return None
    if isinstance(obj, (str, int, float, bool)):
        return obj
    if isinstance(obj, datetime.date):
        return obj.isoformat()
    if isinstance(obj, list):
        return [_serializar(i) for i in obj]    
    if hasattr(obj, "mostrar"):
        return obj.mostrar()
    return repr(obj)

def _imprimir(reg):
    icono = "[OK]" if reg["estado"] == "OK" else "[ERROR]"
    error_info = f" | ERROR: {reg['error']}" if reg["error"] else ""
    print(f"[AUDITORÍA] {icono} {reg['inicio']} | "
          f"{reg['clase']}.{reg['operacion']} | "
          f"{reg['duracion_ms']} ms{error_info}")
    
# DECORADOR

def registrar_operacion(func: Callable) -> Callable:
    
    #Registra en el log de auditoría cada llamada al método decorado.
    #Captura:
    # Nombre de la operación y la clase
    # Argumentos recibidos
    # Timestamp de inicio y fin
    # Duración en milisegundos
    # Resultado devuelto
    # Estado: "OK" o "ERROR" (con mensaje de excepción si aplica)
    #En caso de excepción la registra y la re-lanza sin suprimirla.
    
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs) -> Any:
        nombre_clase = type(self).__name__
        nombre_op    = func.__name__

        args_log   = [_serializar(a) for a in args]
        kwargs_log = {k: _serializar(v) for k, v in kwargs.items()}

        inicio = datetime.datetime.now()
        t0     = time.perf_counter()

        entrada = {
            "operacion"  : nombre_op,
            "clase"      : nombre_clase,
            "args"       : args_log,
            "kwargs"     : kwargs_log,
            "inicio"     : inicio.isoformat(),
            "fin"        : None,
            "duracion_ms": None,
            "resultado"  : None,
            "estado"     : None,
            "error"      : None,
        }

        try:
            resultado = func(self, *args, **kwargs)

            fin = datetime.datetime.now()
            entrada.update({
                "fin"        : fin.isoformat(),
                "duracion_ms": round((time.perf_counter() - t0) * 1000, 3),
                "resultado"  : _serializar(resultado),
                "estado"     : "OK",
            })
            _log_auditoria.append(entrada)
            _imprimir(entrada)
            return resultado

        except Exception as exc:
            fin = datetime.datetime.now()
            entrada.update({
                "fin"        : fin.isoformat(),
                "duracion_ms": round((time.perf_counter() - t0) * 1000, 3),
                "estado"     : "ERROR",
                "error"      : f"{type(exc).__name__}: {exc}",
            })
            _log_auditoria.append(entrada)
            _imprimir(entrada)
            raise  # re-lanza la excepción original


    return wrapper
