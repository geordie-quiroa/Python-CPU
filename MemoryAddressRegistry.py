class MAR:
    def __init__(self, PC=0):
        self.dataAddress2fetch = PC
        self.nextDataAddress2fetch = PC+1

class addressBus(MAR):
    def ramDir(self):
        self.dir = self.dataAddress2fetch
        return self.dir


if __name__=='__main__':
    PC = 2
    MAR = MAR() # puede ir vacio, lo tomaria como PC = 0
    MAR.dataAddress2fetch = PC
    MAR.dataAddress2fetch = 8
    print(addressBus().ramDir())
    ramDir = addressBus.ramDir(MAR)
    print(MAR.dataAddress2fetch)
    print(ramDir)