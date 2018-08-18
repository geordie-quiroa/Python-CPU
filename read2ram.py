class load2ram():

    def readcodefile(self, file):
        readMe=open(file, 'r').read()
        #return readMe
        splitMe=readMe.split('\n') #crea un array
        print(splitMe)


load2ram.readcodefile("test.code")

