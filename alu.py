class ALU:
    def sum(self, high, low):
        return bin(int(high,2) + int(low,2))
    def sub(self, high, low):
        return bin(int(high,2) - int(low, 2))
    def comp(self, high, low):
        result = 0
        if high == low:
            result = 1
        return result
    def shr(self, register):
        return bin(int(register, 2)>>1)
    def shl(self, register):
        return bin(int(register, 2)<<1)

    def rol(self, num, bits = 4):
        num = int(num, 2)
        bit = num & (1 << (bits-1))
        num <<= 1
        if(bit):
            num |= 1
        num &= (2**bits-1)

        return bin(num)

    def ror(self, num, bits = 4):
        num = int(num, 2)
        num &= (2**bits-1)
        bit = num & 1
        num >>= 1
        if(bit):
            num |= (1 << (bits-1))

        return bin(num)

if __name__ == "__main__":
    alu = ALU()    
    print(alu.ror('1001'))