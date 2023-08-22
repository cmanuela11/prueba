class Paciente:
    def __init__(self):
        self.__nombre= ""
        self.__cedula= 0
        self.__servicio= " "
        self.__genero= ""

    def VerNombre(self):
        return self.__nombre
    def VerCedula(self):
        return self.__cedula
    def VerServicio(self):
        return self.__servicio
    def VerGenero(self):
        return self.__genero

    def AsignarNombre(self,n):
        self.__nombre= n
    def AsignarCedula(self,c):
        self.__nombre= c
    def AsignarServicio(self,s):
        self.__nombre= s
    def AsignarGenero(self,g):
        self.__nombre= g
class Sistema:


    def __init__(self):
        self.__lista_pacientes= []
        self.__numero_pacientes=len(self.__lista_pacientes)

    def IngresarPaciente(self,pac):
        self.__lista_pacientes.append(p)
        self.__numero_pacientes=len(self.__lista_pacientes)

    def verificar_cedula(self, cedula):
        for paciente in self.pacientes:
            if paciente.cedula == cedula:
                return True
        else:
            return cedula

    def VerNumeroPacientes(self):
        print("En el sistema hay: "+ str(len(self.__lista_pacientes))+ " pacientes")

    def VerDatosPaciente(self,c):
        for p in self.__lista_pacientes:
            if c==p.verCedula:
                return p

    

def main():
 sis=Sistema()
 while True:
    opcion=(int(input("ingrese la opción que desea realizar: \n 1. ingresar nuevo paciente \n 2.Ver Paciente \n 3.Salir")))
    if opcion == 1:
        c=int(input("Ingrese la cedula del paciente: "))
        r=sis.verificar_cedula(c)
        if r == True:
            print("El paciente esta en nuestra base de datos registrada")
        else:
            print("A continuacion se pediran los datos")
            n=input("Ingrese el nombre del paciente: ")
            g=input("ingrese el genero del paciente: ")
            s=input("Ingrese el servicio del paciente: ")
            pac=Paciente()
            pac.AsignarNombre(n)
            pac.AsignarCedula(c)
            pac.AsignarGenero(g)
            pac.AsignarServicio(s)
            sis.IngresarPaciente(pac)

    elif opcion==2:
        c=int(input("Ingrese la cedula del paciente a buscar: "))
        p=sis.VerDatosPaciente(c)
        print("Nombre: "+ p.verNombre())
        print("Cedula: "+ p.verCedula())
        print("Genero: "+ p.verGenero())
        print("Servicio: "+ p.verServicio())
    elif opcion==3:
        break
    else:
        print("Ingrese una opcion de las indicadas")

if __name__== "__main__":
   main()





   






    
    



    

