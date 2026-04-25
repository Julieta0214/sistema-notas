import pandas as pd
from pathlib import Path

def obtener_ruta_base():
    return Path(__file__).parent

def cargar_estudiantes():
    ruta = obtener_ruta_base() / "data" / "raw" / "estudiantes.txt"
    return pd.read_csv(ruta)

def cargar_profesores():
    ruta = obtener_ruta_base() / "data" / "raw" / "profesores.txt"
    return pd.read_csv(ruta)

def cargar_programas_academicos():
    ruta = obtener_ruta_base() / "data" / "raw" / "programas_academicos.txt"
    return pd.read_csv(ruta)

def cargar_materias():
    ruta = obtener_ruta_base() / "data" / "raw" / "materias.txt"
    return pd.read_csv(ruta)
def cargar_grupos():
    ruta = obtener_ruta_base() / "data" / "raw" / "grupos.txt"
    return pd.read_csv(ruta)

def cargar_matriculas():
    ruta = obtener_ruta_base() / "data" / "raw" / "matriculas.txt"
    return pd.read_csv(ruta)

def cargar_calificaciones():
    ruta = obtener_ruta_base() / "data" / "raw" / "calificaciones.txt"
    return pd.read_csv(ruta)

def cargar_todos_datos():
    datos = {
        'estudiantes': cargar_estudiantes(),
        'profesores': cargar_profesores(),
        'programas_academicos': cargar_programas_academicos(),
        'materias': cargar_materias(),
        'grupos': cargar_grupos(),
        'matriculas': cargar_matriculas(),
        'calificaciones': cargar_calificaciones()
    }
    return datos
