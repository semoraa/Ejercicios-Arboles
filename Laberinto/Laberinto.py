class Arbol():
    def __init__ (self,  valor=0, hijos = []):
        self.valor = valor
        self.hijos = hijos

    def insertar(valor, arbol):
        if arbol == None:
            return Arbol(valor)
        elif buscar(valor, arbol):
            return arbol
        else:
            arbol.hijos.append(Arbol(valor))
            return arbol

        
def cargarArchivo():
    return[list(linea)[:-1] for linea in open ("Laberinto.txt").readlines()]
    
