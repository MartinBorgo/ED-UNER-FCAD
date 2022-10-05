from claseAbstracta_VideoJuegoAdminAbstract import VideojuegosAdminAbstract
from clase_videojuego import VideoJuego
from clase_empresa import Empresa
from clase_genero import Genero

class VideoJuegoAdmin(VideojuegosAdminAbstract):
    def __str__(self):
        texto = ""
        for juegos in self.videojuegos:
            texto += "{juegos}\n".format(juegos=str(juegos.__str__()))
        return texto

    def agregar(self,  videojuego: VideoJuego):
        self.videojuegos.append(videojuego)

    def filtrar_por_desarrolladora(self, desarrolladora: Empresa):
        lista_desarrolladora = []
        for videojuego in self.videojuegos:
            if videojuego.desarrolladora == desarrolladora:
                lista_desarrolladora.append(videojuego)
        
        return lista_desarrolladora

    def filtrar_por_distribuidora(self, distribuidora: Empresa):
        lista_distribuidora = []
        for videojuego in self.videojuegos:
            if videojuego.distribuidora == distribuidora:
                lista_distribuidora.append(videojuego)
        
        return lista_distribuidora

    def filtrar_por_genero(self, genero: Genero):
        lista_genero = []
        for videojuego in self.videojuegos:
            if videojuego.genero == genero:
                lista_genero.append(videojuego)

        return lista_genero

    def cantidad_por_plataforma(self):
        pc = 0
        play = 0
        xbox = 0
        switch = 0
        for videojuego in self.videojuegos:
            lista_plataforma = videojuego.plataforma
            for plataforma in lista_plataforma:
                if "PC" in plataforma.nombre:
                    pc += 1
                
                if "playstation" in plataforma.nombre:
                    play += 1
                
                if "xbox" in plataforma.nombre:
                    xbox += 1

                if "switch" in plataforma.nombre:
                    switch += 1

        return [f"Juegos PC: {pc}", f"Juegos PlayStation: {play}", f"Juegos Xbox: {xbox}", f"Juegos Switch: {switch}"]

    def ordenar_titulo(self):
        self.videojuegos = sorted(self.videojuegos, key= lambda x : x.titulo)

    def ordenar_mejores_primero(self):
        self.videojuegos = sorted(self.videojuegos, key = lambda x : x.ranking, reverse = True)