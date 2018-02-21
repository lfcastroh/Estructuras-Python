class Paciente():
    def __init__(self, nombre, edad, especialidad):
        self.nombre = nombre
        self.edad = edad
        self.especialidad = especialidad


class Cola():
    def __init__(self):
        self.items = []

    def encolar(self, x):
        self.items.append(x)

    def desencolar(self):
        return self.items.pop(0)

    def es_vacia(self):
        return self.items == []


# Sistema de atencion (Colas)
cardiologia = Cola()
heridasGraves = Cola()
heridasLeves = Cola()
neurologia = Cola()
traumatologia = Cola()
psiquiatria = Cola()
listaDeAtencion = [cardiologia, heridasGraves, traumatologia, neurologia, heridasLeves, psiquiatria]

while True:
    accion = raw_input("Ingrese 1 para ingresar paciente, 2 para atender paciente y 0 para salir")
    if accion == "1":
        name = raw_input("Ingrese el nombre del paciente")
        age = raw_input("Ingrese la edad del paciente")
        espec = raw_input("Ingrese la especialidad que solicita el paciente")
        pac = Paciente(name, age, espec)
        if pac != None:
            if pac.especialidad == "cardiologia":
                listaDeAtencion[0].encolar(pac)
                print("Paciente en cola para la categoria de cardiologia")

            if pac.especialidad == "heridas graves":
                listaDeAtencion[1].encolar(pac)
                print("Paciente en cola para la categoria de heridas graves")

            if pac.especialidad == "traumatologia":
                listaDeAtencion[2].encolar(pac)
                print("Paciente en cola para la categoria de traumatologia")

            if pac.especialidad == "neurologia":
                listaDeAtencion[3].encolar(pac)
                print("Paciente en cola para la categoria de neurologia")

            if pac.especialidad == "heridas leves":
                listaDeAtencion[4].encolar(pac)
                print("Paciente en cola para la categoria de heridas leves")

            if pac.especialidad == "psiquiatria":
                listaDeAtencion[5].encolar(pac)
                print("Paciente en cola para la categoria de psiquiatria")
            pac = None
    elif accion == "2":

        if listaDeAtencion[0].es_vacia() == False:
            paceinteAtnedido = listaDeAtencion[0].desencolar()
            print ("Se ha atendido a "+paceinteAtnedido.nombre+" de "+paceinteAtnedido.edad+" en la especialidad de "+paceinteAtnedido.especialidad)
        elif listaDeAtencion[0].es_vacia():
            if listaDeAtencion[1].es_vacia() == False:
                paceinteAtnedido = listaDeAtencion[1].desencolar()
                print ("Se ha atendido a "+paceinteAtnedido.nombre+" de "+paceinteAtnedido.edad+" en la especialidad de "+paceinteAtnedido.especialidad)
            elif listaDeAtencion[1].es_vacia():
                if listaDeAtencion[2].es_vacia() == False:
                    paceinteAtnedido = listaDeAtencion[2].desencolar()
                    print ("Se ha atendido a "+paceinteAtnedido.nombre+" de "+paceinteAtnedido.edad+" en la especialidad de "+paceinteAtnedido.especialidad)
                elif listaDeAtencion[2].es_vacia():
                    if listaDeAtencion[3].es_vacia() == False:
                        paceinteAtnedido = listaDeAtencion[3].desencolar()
                        print ("Se ha atendido a "+paceinteAtnedido.nombre+" de "+paceinteAtnedido.edad+" en la especialidad de "+paceinteAtnedido.especialidad)
                    elif listaDeAtencion[3].es_vacia():
                        if listaDeAtencion[4].es_vacia() == False:
                            paceinteAtnedido = listaDeAtencion[4].desencolar()
                            print ("Se ha atendido a "+paceinteAtnedido.nombre+" de "+paceinteAtnedido.edad+" en la especialidad de "+paceinteAtnedido.especialidad)
                        elif listaDeAtencion[4].es_vacia():
                            print ("NO hay pacientes por atender")
        
    elif accion == "0":
        break