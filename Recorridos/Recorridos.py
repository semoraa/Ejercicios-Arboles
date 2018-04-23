class Arbol:
    def __init__ (self,  val=0, izq=None, der=None):
        self.valor = val
        self.izquierda = izq
        self.derecha = der

def inorden(arbol):
    if arbol == None:
        return []
    else:
        return inorden(arbol.izquierda) + [arbol.valor] + inorden(arbol.derecha)

def preorden(arbol):
     if arbol == None:
        return []
     else:
        return [arbol.valor] + preorden(arbol.izquierda) + preorden(arbol.derecha)

def posorden(arbol):
    if arbol == None:
        return []
    else:
        return posorden(arbol.izquierda) + posorden(arbol.derecha) + [arbol.valor]

arbol= Arbol(10, Arbol(5),Arbol(50, Arbol(30, Arbol(20), Arbol(40))))

print(inorden(arbol))
print(preorden(arbol))
print(posorden(arbol))
