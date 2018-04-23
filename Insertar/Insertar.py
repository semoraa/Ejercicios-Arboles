class Arbol:
    def __init__ (self,  val=0, izq=None, der=None):
        self.valor = val
        self.izquierda = izq
        self.derecha = der

def buscar(valor, arbol):
            if arbol == None:
                return False
            if arbol.valor == valor:
                return True
            if valor > arbol.valor:
                return buscar(valor, arbol.derecha)
            return buscar(valor, arbol.izquierda)

def inorden(arbol):
    if arbol == None:
        return []
    else:
        return inorden(arbol.izquierda) + [arbol.valor] + inorden(arbol.derecha)

def insertar(valor, arbol):
    if arbol == None:
        return Arbol(valor)
    if valor < arbol.valor:
        return Arbol(arbol.valor, insertar(valor, arbol.izquierda) , arbol.derecha)
    return Arbol(arbol.valor, arbol.izquierda, insertar(valor, arbol.derecha))

arbol= Arbol(10, Arbol(5),Arbol(50, Arbol(30, Arbol(20), Arbol(40))))



print(inorden(arbol))
print(inorden(insertar(75,arbol)))
