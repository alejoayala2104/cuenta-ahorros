# AUTOR: ALEJANDRO AYALA - 219034431

class Usuario:
    def __init__(self, nombre, apellido, cedula, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.edad = edad
        
class Cuenta(Usuario):
    def __init__(self, nombre, apellido, cedula, edad, dineroAhorrado):
        super().__init__(nombre, apellido, cedula, edad)
        self.dineroAhorrado = dineroAhorrado
        
    def getNombre(self): return self.nombre
    def setNombre(self, nombre): self.nombre = nombre
    
    def getApellido(self): return self.apellido
    def setApellido(self, apellido): self.apellido = apellido
    
    def getCedula(self): return self.cedula
    def setCedula(self, cedula): self.cedula = cedula
    
    def getEdad(self): return self.edad
    def setEdad(self, edad): self.edad = edad
    
    def getDineroAhorrado(self): return self.dineroAhorrado
    def setDineroAhorrado(self, dineroAhorrado): self.dineroAhorrado = dineroAhorrado
        
    def mostrar(self):
        return f'Resumen de Usuario\n - Nombres: {self.nombre} {self.apellido}\n - Cedula: {self.cedula}\n - Edad: {self.edad}\n - Dinero ahorrado: {self.dineroAhorrado}'
    
    def ingresar(self, consignacion):
        if(not consignacion or consignacion < 0):
            print("ERROR! La consignacion debe ser un número positivo.")
            return
        self.dineroAhorrado += consignacion
    
    def retirar(self, retiro):
        if(not retiro or (self.dineroAhorrado - retiro < 0) or retiro < 0):
            print("ERROR! La cuenta no tiene suficiente dinero para realizar dicho retiro.")
            return
        self.dineroAhorrado -= retiro
        print(f'Retirando...\nDinero restante: {self.dineroAhorrado}')

class Beneficio(Cuenta):
    def __init__(self, nombre, apellido, cedula, edad, dineroAhorrado, pInteres):
        super().__init__(nombre, apellido, cedula, edad, dineroAhorrado)
        self.pInteres = pInteres
    
    def usuarioCorrecto(self):
       return (self.edad >= 18 and self.edad < 28)
    
    def mostrarBeneficio(self):
        if(not self.usuarioCorrecto()):
            return "El usuario no es beneficiario"
        return f'Dinero en la cuenta: {self.dineroAhorrado}\nTotal con beneficio: {self.dineroAhorrado + (self.dineroAhorrado * self.pInteres)}'
    
# if __name__ == "__main__":
#     beneficio = Beneficio("Alejandro", "Ayala", "1233191314", 2, 1000000, 0.05)
#     beneficio.ingresar(1500000)
#     print(beneficio.mostrar())
#     print("======================")
#     beneficio.retirar(500000)
#     print(beneficio.mostrarBeneficio())
#     print("======================")
#     print(beneficio.mostrar())
    