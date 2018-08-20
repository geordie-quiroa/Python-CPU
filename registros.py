class registers:
    inUse = 0 #cuando se consulta dice cuantos registros tienen un valor distinto a cero; estan en uso

    def __init__(self, n=0):
        if n == 0:
            self.storedValue = n # el valor en el registro es cero
        else:
            self.storedValue = n # asigna el valor contenido al objeto del registro
            registers.inUse += 1 # cambia el contador que esta al inicio de la clases para saber que hay un registro mas en uso

    def clearRegistry(self): 
        self.storedValue = 0 #cuando el CU termine de usar ese registro, utilizar este metodo
        registers.inUse -= 1

    def withValue(self): # va a retornar si un registro en especifico tiene un valor almacenado.
        if self.storedValue > 0:
            return 1
        else:
            return 0