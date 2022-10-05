from clase_genero import Genero
from clase_plataforma import Plataforma
from clase_empresa import Empresa
from datetime import datetime


class VideoJuego():
    def __init__(self, titulo: str, genero: Genero, plataforma: list, descripcion: str, precio: float, desarrolladora: Empresa, distribuidora: Empresa, fecha_lanzamiento: datetime, ranking: float):
        if ranking < 0 or ranking > 10:
            raise Exception("Numero de ranking invalido")
        else:
            self.titulo = titulo
            self.genero = genero
            self.plataforma = plataforma
            self.descripcion = descripcion
            self.precio = precio
            self.desarrolladora = desarrolladora
            self.distribuidora = distribuidora
            self.fecha_lanzamiento = fecha_lanzamiento
            self.ranking = ranking

    def __str__(self):
        return "Titlulo: %s, Genero: %s, Plataforma -> %s, Descirpcion: %s, Precio: %d, Desarrolladora -> %s, Distribuidor -> %s, Fecha de lanzamiento: %s, Ranking: %d" %(self.titulo, self.genero, self.plataforma, self.descripcion,self.precio, self.desarrolladora.__str__(), self.distribuidora.__str__(), self.fecha_lanzamiento, self.ranking)

    def __repr__(self):
        return "Este objeto es de clase {}".format(self.__class__.__name__)

    def __eq__(self, other):
        if isinstance(other, VideoJuego):
            return self.titulo == other.titulo