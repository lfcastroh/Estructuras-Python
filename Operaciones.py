class Pila:
 
    def __init__(self):
        self.items=[]

    def apilar(self, x):
        self.items.append(x)

    def desapilar(self):
        try:
            return self.items.pop()
        except IndexError:
            raise ValueError("La pila está vacía")

    def es_vacia(self):
        return self.items == []

class Operacion():
    def operar(self, x):
        operacion=Pila()
        i=0
        ope=x.split(" ")
        
        while i < len(ope):
                if ope[i]!="+" or ope[i]!="-" or ope[i]!="*" or ope[i]!="/" :
                    operacion.apilar(ope[i])
                    i=i+1
                if ope[i]=="+" or ope[i]=="-" or ope[i]=="*" or ope[i]=="/" :
                    z=int(operacion.desapilar())
                    y=int(operacion.desapilar())
                    if ope[i]=="+":
                        res=z+y
                        operacion.apilar(res)
                    if ope[i]=="-":
                        res=z-y
                        operacion.apilar(res)
                    if ope[i]=="*":
                        res=z*y
                        operacion.apilar(res)
                    if ope[i]=="/":
                        res=z/y
                        operacion.apilar(res)
                    i=i+1
        
        return operacion.desapilar()

oper = raw_input("Ingrese operacion en posfijo: ")
lista = Operacion()
x=lista.operar(oper)

print(x)