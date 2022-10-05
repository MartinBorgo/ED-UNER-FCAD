from enum import Enum

class Colores(Enum):
    ROJO = 1
    VERDE = 2
    AZUL = 3


algo = Colores.AZUL
otro_algo = Colores.AZUL

if algo == otro_algo:
    print("si")