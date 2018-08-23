class ALU:
    # Todas las funciones del ALU retornan un binario    
    def sum(self, high, low):
        # Convierte la parte alta y baja del registro a un integer y lo suma
        # Despues convierte la suma a binario
        return bin(int(high,2) + int(low,2))

    def sub(self, high, low):
        # Convierte la parte alta y baja del registro a un integer y lo resta
        # Despues convierte la suma a binario
        return bin(int(high,2) - int(low, 2))

    def comp(self, high, low):
        # Si la comparacion no es igual retorna 0
        # Sirve para poder hacer un JMP_N, compara la parte alta y baja de un registro
        result = 1
        if high != low:
            result = 0
        return result

    def shr(self, register):
        # Convierte el registro a integer
        # Hace un shift a la derecha
        # Retorna el binario del resultado
        return bin(int(register, 2)>>1)

    def shl(self, register):
        # Convierte el registro a integer
        # Hace un shift a la izquierda
        # Retorna el binario del resultado
        return bin(int(register, 2)<<1)

    def rol(self, register, bits = 4):
        # Convierte el registro a integer
        register = int(register, 2)
        # Hace un Y logico con el registro y un shift right del binario componente
        bit = register & (1 << (bits-1))
        # Shift logico a la izquierda del registro
        register <<= 1
        if(bit):
            register |= 1
        # Y logico entre el registro y la potencia del componente binario
        register &= (2**bits-1)

        # Retornar en binario
        return bin(register)

    def ror(self, register, bits = 4):
        # La misma logica que el anterior pero para Shift Right
        register = int(register, 2)
        register &= (2**bits-1)
        bit = register & 1
        register >>= 1
        if(bit):
            register |= (1 << (bits-1))

        return bin(register)

if __name__ == "__main__":
    alu = ALU()
    print(alu.ror('1001'))